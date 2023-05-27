from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    watchlist = models.ManyToManyField('AuctionListing', blank=True, related_name='watchlisted_by')


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class AuctionListing(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=350)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.ForeignKey('Bid', on_delete=models.SET_NULL, null=True, blank=True, related_name='listing_bids')
    image_url = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='listings')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='listings')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bid by {self.bidder.username} on {self.listing.title}"


class Comment(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.listing.title}"
