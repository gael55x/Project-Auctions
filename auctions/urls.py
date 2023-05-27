from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listings/create/', views.create_listing, name='create_listing'),
    path("listings/<int:listing_id>/", views.listing, name="listing"),
    path("listings/<int:listing_id>/close/", views.close_auction, name="close_auction"),
    path("listings/<int:listing_id>/place/", views.place_bid, name="place_bid"),
    path("listings/<int:listing_id>/comment/", views.add_comment, name="add_comment"),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/remove/<int:listing_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
]
