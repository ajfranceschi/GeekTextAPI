# ===============================================================
# Created by: Antonio J. Franceschi
#
# This file contains the database queries for GeekText API
# Book Browsing and Sorting feature
# ===============================================================
from models.db_book_model import Books, booksSchema
from sqlalchemy.exc import SQLAlchemyError


# Get all books currently in the database
def getBooks(arg: int = 0):
    if arg == 0:
        try:
            return Books.query.all()
        except SQLAlchemyError as e:
            print(e)
            return "error"


def getBooksStartingAt(position: int):
    selection: list = []
    booksQueryResult: dict = getBooks()
    booksQueryLength: int = len(booksQueryResult)

    if booksQueryResult != "error":
        if booksQueryLength >= position:
            left: int = position - 1
            right: int = left + position
            if right > booksQueryLength - 1:
                # set right to be the end of the list
                right = booksQueryLength - 1

            for idx in range(left, right + 1, 1):
                selection.append(booksQueryResult[idx])

            return selection
        else:
            return "request-error"
    else:
        return booksQueryResult


def booksByGenre(genre: str):
    books = booksSchema.dump(getBooks())
    res = []
    genres = {
            "!Error": f"No books found for genre {genre}. Here are the available genres:"
    }

    for book in books:
        bookGenre = book["bookGenre"]
        bookGenreTitled = bookGenre.title()

        if not genres.__contains__(bookGenreTitled):
            genres[bookGenreTitled] = 1
        else:
            genres[bookGenreTitled] = genres[bookGenreTitled] + 1

        if bookGenre == genre:
            res.append(book)

    if len(res) > 0:
        return res
    else:
        return genres


def booksWithRatingAtOrAbove(rating):
    books = booksSchema.dump(getBooks())
    res = []
    for book in books:
        if book['bookRating'] >= rating:
            res.append(book)

    return res


def getOptions():
    root: str = 'http://localhost:81/books'  # TODO: Update VIEWS.py to reflect this URL
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
                    "top-ten": {
                            "URL": f'{root}/top-ten',
                            "methods": "GET",
                            "Description": 'Returns the top-ten sold books.',
                            "Params": {},
                            "Examples": {
                                    "Get top-ten sold books": f'GET {root}/top-ten'
                            }
                    },
                    "by-genre": {
                            "URL": f'{root}/by-genre',
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
                    "by-rating": {
                            "URL": f'{root}/by-rating',
                            "methods": "GET",
                            "Description": 'Provide the parameter <genre> to obtain the books categorized in the'
                                           ' provided genre.',
                            "Params": {
                                    "genre": "Book genre to be searched.",
                            },
                            "Examples": {
                                    "Get books by genre": f'GET {root}/by-rating?genre=Fantasy'
                            }
                    }
            }
    }
