from flask import jsonify, request

from models.db_book_model import booksSchema
from . import bkBrowseSort_bp, book_browsing_util

# CONSTANTS
SERVER_ERROR = "Could not complete the request. Please try again later", 500
QUANTITY_ERROR = "To obtain a list of books set the <quantity> parameter to an int greater than 0", 400
PARAM_ERROR = "Params are not accurate. Please check your params", 400


# Root Book Browsing and Sorting endpoint: (*/book-browsing-sorting/)
@bkBrowseSort_bp.route('/', methods = ['GET', 'OPTIONS'])
def index():
    if request.method == 'OPTIONS':
        return book_browsing_util.getOptions()
    else:
        return "Books Browsing and Sorting root", 200


# Book Browsing and Sorting / Get All Books endpoint: (*/book-browsing-sorting/get-books)
@bkBrowseSort_bp.route('/get-books')
def get_books():
    params = request.args
    print(len(params))

    ## include arguments
    if len(request.args) > 0:
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
        books = book_browsing_util.getBooks()
        if books == "error":
            return SERVER_ERROR
        return jsonify(booksSchema.dump(books)), 200


# Book Browsing and Sorting / Get top 10 books sold endpoint: (*/book-browsing-sorting/top-ten-books-sold)
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


@bkBrowseSort_bp.route('/by-genre', methods = ['GET'])
def books_by_genre():
    genre = request.args['genre']
    books = book_browsing_util.booksByGenre(genre)
    return jsonify(books)


# UTILITY FUNCTIONS
def sortByUnitsSold(book: dict):
    return book["unitsSold"]
