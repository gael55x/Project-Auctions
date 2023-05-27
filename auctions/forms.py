from django import forms
from .models import AuctionListing, Category

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category', 'current_bid']
