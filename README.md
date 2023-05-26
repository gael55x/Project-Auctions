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

> Note: You can change it lol.

## Features

- **Create Listing**: Users have the ability to create new auction listings by providing essential details such as title, description, starting bid, and optional information like image URL and category selection.
- 
- **Active Listings Page**: The default route presents users with a comprehensive view of all currently active auction listings. Each listing showcases key information such as title, description, current price, and, if available, an associated photo.

- **Listing Page**: Clicking on a specific listing leads users to a dedicated page that provides comprehensive details about the listing, including the current price and other relevant information.

- **Watchlist**: Signed-in users can curate their personalized watchlist by adding and removing listings according to their preferences. The watchlist page showcases all the listings that a user has added, and clicking on any listing redirects the user to its respective page.

- **Bidding**: Authenticated users can participate in the bidding process by placing bids on auction listings. The bid amount must be equal to or higher than the starting bid and any existing bids. Users are promptly notified and presented with an error if the bid does not meet these criteria.

- **Closing Auction**: Listing creators who are signed in have the privilege to "close" auctions directly from the listing page. This action determines the highest bidder as the winner and marks the listing as inactive.

- **Winning Status**: On a closed listing page, if a signed-in user emerges as the winner of the auction, their winning status is prominently displayed.

- **Comments**: Authenticated users can engage in discussions and provide comments on listing pages. All comments made by users on a listing are dynamically displayed on the page, facilitating interaction and conversation.

- **Categories**: Users can explore a dedicated page that showcases a comprehensive list of all available listing categories. Clicking on a specific category directs the user to a page displaying all active listings within that category.

- **Django Admin Interface**: The Django admin interface empowers site administrators with extensive capabilities to manage the platform effectively. Administrators can effortlessly view, add, edit, and delete listings, comments, and bids within the system.

## How to Run in VSC
To run the Project-Auctions web app in Visual Studio Code (VSC), follow these steps:

1. Make a virtual environment by executing the following command in your terminal:
  - **python3 -m venv venv**

2. Activate the virtual environment by running the appropriate command based on your operating system:
   - **Windows**:
      venv\Scripts\activate
   - **MacOS/Linux**:
      source venv/bin/activate
      
3. If you haven't installed virtualenv, use the following command:
  pip install virtualenv
  
  
Now you can proceed with setting up and running the Project-Auctions web app in VSC.

