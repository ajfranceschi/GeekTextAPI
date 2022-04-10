# ===============================================================
# Created by: Antonio J. Franceschi
#
# This file contains the routes for GeekText API
# Book Browsing and Sorting feature
# ===============================================================

from flask import jsonify, request

from models.db_book_model import booksSchema
from . import bkBrowseSort_bp, book_browsing_util

# CONSTANTS
SERVER_ERROR = {'!Error': 'Could not complete the request. Please try again later'}, 500
QUANTITY_ERROR = {'!Error': 'To obtain a list of books set the <quantity> parameter to an int greater than 0'}, 400
PARAM_ERROR = {'!Error': 'Params are not accurate. Please check your params'}, 400
FLOAT_ERROR = {'!Error': 'To obtain a list of books based on rating, set the <rating> parameter '
                         'to a float greater than or equal to 0.0 and less than or equal to 5.0'}, 400


# Root Book Browsing and Sorting endpoint: (*/book-browsing-sorting/)
@bkBrowseSort_bp.route('/', methods = ['GET', 'OPTIONS'])
def index():
    if request.method == 'OPTIONS':
        return book_browsing_util.getOptions()
    else:
        return "Books Browsing and Sorting root", 200


# Book Browsing and Sorting / Get All Books / Get X amount of Books beginning at X position:
# (*/book-browsing-sorting/get-books)
@bkBrowseSort_bp.route('/get-books')
def get_books():
    params = request.args
    print(len(params))

    # include arguments
    if len(params) > 0:
        # Get X amount of Books beginning at X Position.
        for param in params:
            print(param)
        try:
            quantity = int(request.args['quantity'])
            # validate quantity is an int:
            if type(quantity) == int and quantity > 0:
                books = book_browsing_util.getBooksStartingAt(quantity)
                if books == "error":  # Error connecting to DB
                    return SERVER_ERROR
                elif books == "request-error":  # quantity provided is greater than amount of books in DB
                    return f"Quantity parameter should be less than {len(book_browsing_util.getBooks()) + 1}."
                return jsonify(booksSchema.dump(books))
            else:
                return QUANTITY_ERROR
        except ValueError as e:
            print(e)
            return PARAM_ERROR
    else:
        # Get All Books in DB
        books = book_browsing_util.getBooks()
        if books == "error":
            return SERVER_ERROR
        return jsonify(booksSchema.dump(books)), 200


# Book Browsing and Sorting / Get top 10 books sold endpoint: (*/book-browsing-sorting/top-ten)
@bkBrowseSort_bp.route('/top-ten')
def top_ten_books_sold():
    booksQuery = book_browsing_util.getBooks()

    if booksQuery == "error":
        return 'There was an error getting the list. Please try again later.', 500
    elif len(booksQuery) == 0:
        return SERVER_ERROR
    else:
        books: list = booksSchema.dump(booksQuery)
        sortedBooks: list = sorted(books, key = sortByUnitsSold, reverse = True)

        if len(booksQuery) > 10:
            topTenBooks: list = []
            for idx in range(0, 10, 1):
                topTenBooks.append(sortedBooks[idx])
            return jsonify(topTenBooks)
        else:
            return jsonify(sortedBooks)


# Book Browsing and Sorting / Get Books by Genre: (*/book-browsing-sorting/by-genre)
# Route to return books that match the provided Genre or a list of available Genres
@bkBrowseSort_bp.route('/by-genre', methods = ['GET'])
def books_by_genre():
    genre = request.args['genre'].title()
    books = book_browsing_util.booksByGenre(genre)
    return jsonify(books), 200


# Book Browsing and Sorting / Get Books by Rating: (*/book-browsing-sorting/by-rating)
# Route to return books that have a rating greater than or equal to the rating provided by user.
@bkBrowseSort_bp.route('by-rating', methods = ['GET'])
def by_rating():
    try:
        rating = float(request.args['rating'])
        if rating < 0 or rating > 5:
            return FLOAT_ERROR
        books = book_browsing_util.booksWithRatingAtOrAbove(rating)
        return jsonify(books)
    except ValueError as e:
        return FLOAT_ERROR


# UTILITY FUNCTIONS
def sortByUnitsSold(book: dict):
    return book["unitsSold"]
