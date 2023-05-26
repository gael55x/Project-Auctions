# Project-Auctions

An auction platform where users can create and manage auction listings, participate in bidding, engage in discussions through comments, and keep track of preferred listings with a personalized watchlist feature. It's built using the Django framework.

## Models

The application includes the following models in addition to the User model:

### Listing
Represents an auction listing and contains the following fields:

- `title`: Title of the listing.
- `description`: Text-based description of the listing.
- `starting_bid`: Starting bid for the listing.
- `image_url` (optional): URL for an image associated with the listing.
- `category` (optional): Category of the listing (e.g., Fashion, Toys, Electronics, Home, etc.).

### Bid
Represents a bid made on an auction listing and includes the following fields:

- `listing`: Foreign key reference to the associated listing.
- `bidder`: Foreign key reference to the user who placed the bid.
- `amount`: The amount of the bid.

### Comment
Represents a comment made on an auction listing and contains the following fields:

- `listing`: Foreign key reference to the associated listing.
- `commenter`: Foreign key reference to the user who made the comment.
- `content`: The text content of the comment.

> Note: You may have additional models depending on your specific requirements.

## Features

- **Create Listing**: Users can visit a page to create a new listing by providing a title, description, starting bid, optional image URL, and category.

- **Active Listings Page**: The default route allows users to view all currently active auction listings. Each listing displays the title, description, current price, and associated photo (if available).

- **Listing Page**: Clicking on a listing takes users to a specific page for that listing. Here, users can view all the details of the listing, including the current price.

- **Watchlist**: Signed-in users can add listings to their watchlist and remove them if they are already added. The watchlist page displays all the listings that a user has added, and clicking on any listing takes the user to its respective page.

- **Bidding**: Signed-in users can place bids on auction listings. The bid must be equal to or higher than the starting bid and any existing bids. Users are presented with an error if the bid does not meet these criteria.

- **Closing Auction**: If the user who created the listing is signed in, they have the ability to "close" the auction from the listing page. This action makes the highest bidder the winner and makes the listing inactive.

- **Winning Status**: On a closed listing page, if a signed-in user has won the auction, the page indicates their winning status.

- **Comments**: Signed-in users can add comments to listing pages, and all comments made on a listing are displayed on the page.

- **Categories**: Users can visit a page that displays a list of all listing categories. Clicking on a category name takes the user to a page showing all active listings in that category.

- **Django Admin Interface**: The Django admin interface allows site administrators to view, add, edit, and delete listings, comments, and bids made on the site.

## How to Run in VSC
To run the Project-Auctions web app in Visual Studio Code (VSC), follow these steps:

1. Make a virtual environment by executing the following command in your terminal:
  python3 -m venv venv

2. Activate the virtual environment by running the appropriate command based on your operating system:
   - **Windows**:
      venv\Scripts\activate
   - **MacOS/Linux**:
      source venv/bin/activate
      
3. If you haven't installed virtualenv, use the following command:
  pip install virtualenv
  
  
Now you can proceed with setting up and running the Project-Auctions web app in VSC.

