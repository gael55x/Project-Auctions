from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import User, AuctionListing, Category, Bid, Comment
from .forms import CreateListingForm

def index(request):
    active_listings = AuctionListing.objects.filter(active=True)
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        active_listings = active_listings.filter(category__id=selected_category)

    return render(request, 'auctions/index.html', {
        'listings': active_listings,
        'categories': categories,
    })

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.creator = request.user
            listing.save()
            bid = Bid(listing=listing, bidder=request.user, amount=listing.starting_bid)
            bid.save()
            listing.current_bid = bid
            listing.active = True
            listing.save()
            messages.success(request, 'Listing created successfully.')
            return redirect('index')
    else:
        form = CreateListingForm()

    return render(request, 'auctions/create_listing.html', {'form': form})

def listing(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id)
    user = request.user
    is_watchlisted = user.is_authenticated and user.watchlist.filter(pk=listing_id).exists()
    has_won = listing.active and listing.current_bid and listing.current_bid.bidder == user

    bids = Bid.objects.filter(listing=listing).order_by('-amount')
    comments = Comment.objects.filter(listing=listing).order_by('-created_at')

    if request.method == 'POST' and user.is_authenticated:
        if 'add_to_watchlist' in request.POST:
            listing_id = request.POST.get('listing_id')
            listing = get_object_or_404(AuctionListing, pk=listing_id)
            if not user.watchlist.filter(pk=listing_id).exists():
                user.watchlist.add(listing)
                messages.success(request, 'Listing added to watchlist.')
            return redirect('watchlist')

        if 'place_bid' in request.POST:
            amount = request.POST.get('bid_amount')
            if amount:
                try:
                    amount = float(amount)
                    if amount >= listing.starting_bid and (not listing.current_bid or amount > listing.current_bid.amount):
                        bid = Bid(listing=listing, bidder=user, amount=amount)
                        bid.save()
                        listing.current_bid = bid
                        listing.save()
                        messages.success(request, 'Bid placed successfully.')
                    else:
                        messages.error(request, 'Invalid bid amount.')
                except ValueError:
                    messages.error(request, 'Invalid bid amount.')

            return redirect('listing', listing_id=listing_id)

        if 'close_auction' in request.POST:
            if listing.creator == user and listing.active:
                if listing.current_bid:
                    listing.active = False
                    listing.save()
                    messages.success(request, 'Auction closed. Winner: {}'.format(listing.current_bid.bidder.username))
                else:
                    messages.error(request, 'Cannot close auction without any bids.')
            else:
                messages.error(request, 'Invalid request.')

            return redirect('listing', listing_id=listing_id)

    return render(request, 'auctions/listing.html', {
        'listing': listing,
        'bids': bids,
        'comments': comments,
        'is_watchlisted': is_watchlisted,
        'has_won': has_won
    })


@login_required
def close_auction(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id)
    if listing.creator == request.user and listing.active:
        if listing.current_bid:
            listing.active = False
            listing.save()
            messages.success(request, 'Auction closed. Winner: {}'.format(listing.current_bid.bidder.username))
        else:
            messages.error(request, 'Cannot close auction without any bids.')
    else:
        messages.error(request, 'Invalid request.')
    return redirect('listing', listing_id=listing_id)

@login_required
def place_bid(request, listing_id):
    if request.method == 'POST':
        listing = get_object_or_404(AuctionListing, pk=listing_id)
        user = request.user
        amount = request.POST.get('bid_amount')
        if amount:
            try:
                amount = float(amount)
                if amount >= listing.starting_bid and (not listing.current_bid or amount > listing.current_bid.amount):
                    bid = Bid(listing=listing, bidder=user, amount=amount)
                    bid.save()
                    listing.current_bid = bid
                    listing.save()
                    messages.success(request, 'Bid placed successfully.')
                else:
                    messages.error(request, 'Invalid bid amount.')
            except ValueError:
                messages.error(request, 'Invalid bid amount.')

        return redirect('listing', listing_id=listing_id)

    return redirect('listing', listing_id=listing_id)

@login_required
def add_comment(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')

        if comment_text:
            comment = Comment(
                listing=listing,
                commenter=request.user,
                text=comment_text
            )
            comment.save()
            messages.success(request, 'Comment added successfully.')
        else:
            messages.error(request, 'Invalid comment.')

    return redirect('listing', listing_id=listing_id)

@login_required
def watchlist(request):
    if request.method == 'POST':
        user = request.user
        listing_id = request.POST.get('add_to_watchlist') or request.POST.get('remove_from_watchlist')
        listing = get_object_or_404(AuctionListing, pk=listing_id)

        if 'add_to_watchlist' in request.POST:
            user.watchlist.add(listing)
            messages.success(request, 'Listing added to watchlist.')
        else:
            user.watchlist.remove(listing)
            messages.success(request, 'Listing removed from watchlist.')

        return redirect('watchlist')

    user = request.user
    watchlist_items = user.watchlist.all()

    return render(request, 'auctions/watchlist.html', {
        'watchlist_items': watchlist_items
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def remove_from_watchlist(request, listing_id):
    if request.method == 'POST':
        user = request.user
        listing = get_object_or_404(AuctionListing, pk=listing_id)
        user.watchlist.remove(listing)
        messages.success(request, 'Listing removed from watchlist.')

    return redirect('watchlist')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
