# ===============================================================
# Created by: Antonio J. Franceschi
#
# This file will hod the database queries for GeekText API
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
    booksQueryResult = getBooks()
    booksQueryLength = len(booksQueryResult)

    if booksQueryResult != "error":
        if booksQueryLength >= position:
            left = position - 1
            right = left + position
            if right > booksQueryLength - 1:
                # set right to be the end of the list
                right = booksQueryLength - 1

            for idx in range(left, right + 1, 1):
                selection.append(booksQueryResult[idx])

            return booksSchema.dump(selection)
        else:
            return "request-error"
    else:
        return booksQueryResult


def booksByGenre(genre: str):
    books = getBooks()
    res = []
    for book in books:
        if book['bookGenre'] == genre:
            res.append(book)

    return res

# TODO: books by genre, particular rating and higher
