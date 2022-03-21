from flask import jsonify, abort, request, Response
from . import bkBrowseSort_bp
from models.db_book_model import Books, booksSchema

# CONSTANTS
SERVER_ERROR = "Could not complete the request. Please try again later", 500
QUANTITY_ERROR = "To obtain a list of books set the <quantity> parameter to an int greater than 0", 400
PARAM_ERROR = "Params are not accurate. Please check your params", 400


# Root Book Browsing and Sorting endpoint: (*/book-browsing-sorting/)
@bkBrowseSort_bp.route('/', methods = ['GET', 'OPTIONS'])
def index():
    if request.method == 'OPTIONS':
        root: str = 'http://localhost:81/book-browsing-sorting'
        return {
                "endpoints": {
                        "/": {
                                "URL": f'{root}',
                                "methods": "GET, OPTIONS",
                                "Description": {
                                        "GET": "Returns text validating connectivity",
                                        "OPTIONS": "Returns the endpoints and instructions of this API."
                                },
                                "Examples": {
                                        "Check connectivity": f"GET {root}",
                                        "Obtain endpoints": f'OPTIONS {root}'
                                }
                        },
                        "get-books": {
                                "URL": f'{root}/get-books',
                                "methods": "GET",
                                "Description": 'Returns all books in the database if no parameters are provided.  '
                                               'Provide the parameter <quantity>(int) to obtain N amount of books'
                                               ' starting at N position in the database. Provide the parameter <genre> '
                                               'to obtain the books categorized as the provided genre.',
                                "Params": {
                                        "quantity": "Amount of books requested beginning at the database's <quantity> "
                                                    "position."
                                },
                                "Examples": {
                                        "Get all books": f'GET {root}/get-books',
                                        "Get n amount of books": f'GET {root}/get-books?quantity=10',
                                }
                        },
                        "genre": {
                                "URL": f'{root}/genre',
                                "methods": "GET",
                                "Description": 'Provide the parameter <genre> to obtain the books categorized in the'
                                               ' provided genre.',
                                "Params": {
                                        "genre": "Book genre to be searched.",
                                },
                                "Examples": {
                                        "Get books by genre": f'GET {root}/genre?genre=sci-fi'
                                }
                        },
                        "top-ten": {
                                "URL": f'{root}/top-ten',
                                "methods": "GET",
                                "Description": 'Returns the top-ten sold books.',
                                "Params": {},
                                "Examples": {
                                        "Get top-ten sold books": f'GET {root}/top-ten'
                                }
                        }
                }
        }
    else:
        return "Books Browsing and Sorting root", 200


# Book Browsing and Sorting / Get All Books endpoint: (*/book-browsing-sorting/get-books)
@bkBrowseSort_bp.route('/get-books')
def get_books():
    if len(request.args) > 0:
        quantity = None
        try:
            quantity = int(request.args['quantity'])
            # validate quantity is an int:
            if type(quantity) == int and quantity > 0:
                # TODO: Get n Books starting at n index
                books = getBooksStartingAt(quantity)
                if books == "error":  # Error connecting to DB
                    return SERVER_ERROR
                elif books == "request-error":  # quantity provided is greater than amount of books in DB
                    return f"Quantity parameter should be less than {len(getAllBooks()) + 1}."
                return jsonify(books)
            else:
                return QUANTITY_ERROR
        except Exception as e:
            return PARAM_ERROR
    else:
        books = getAllBooks()
        if books == "error":
            return SERVER_ERROR
        booksList = booksSchema.dump(books)
        return jsonify(booksList), 200


# Book Browsing and Sorting / Get top 10 books sold endpoint: (*/book-browsing-sorting/top-ten-books-sold)
@bkBrowseSort_bp.route('/top-ten')
def top_ten_books_sold():
    booksQuery = None

    try:
        booksQuery = Books.query.all()
    except Exception as e:
        return 'There was an error getting the list. Please try again later.', 500

    books: list = booksSchema.dump(booksQuery)
    sortedBooks: list = sorted(books, key = sortByUnitsSold, reverse = True)

    # check size of sortedBooks.  If greater than 10, return only top ten, else return sorted books
    if len(sortedBooks) == 0:
        return abort(500, 'There was an error getting the list. Please try again later.')
    elif len(sortedBooks) > 10:
        topTenBooks: list = []
        for idx in range(0, 10, 1):
            topTenBooks.append(sortedBooks[idx])
        return jsonify(topTenBooks)
    else:
        return jsonify(sortedBooks)


@bkBrowseSort_bp.route('/books-by-genre/genre', methods = ['POST'])
@bkBrowseSort_bp.route('/books')
# UTILITY FUNCTIONS
def sortByUnitsSold(book: dict):
    return book["unitsSold"]


def getAllBooks():
    try:
        query = Books.query.all()
        return query
    except Exception as e:
        return "error"


def getBooksStartingAt(position: int):
    booksQuery = getAllBooks()
    if booksQuery != "error":
        if len(booksQuery) >= position:
            left = position - 1
            right = left + position
            if right > len(booksQuery) - 1:
                right = len(booksQuery) - 1
            selection = []
            for idx in range(left, right + 1, 1):
                selection.append(booksQuery[idx])
            return booksSchema.dump(selection)
        else:
            return "request-error"
    else:
        return booksQuery
