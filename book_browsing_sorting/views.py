from flask import jsonify
from . import bkBrowseSort_bp
from models.db_book_model import Books, booksSchema


# Root Book Browsing and Sorting endpoint: (*/book-browsing-sorting/)
@bkBrowseSort_bp.route('/')
def index():
    return "Books Browsing and Sorting root"


# Book Browsing and Sorting / Get All Books endpoint: (*/book-browsing-sorting/get-books)
@bkBrowseSort_bp.route('/get-books')
def get_books():
    booksQuery = Books.query.all()
    booksList = booksSchema.dump(booksQuery)
    return jsonify(booksList)


# Book Browsing and Sorting / Get top 10 books sold endpoint: (*/book-browsing-sorting/top-ten-books-sold)
@bkBrowseSort_bp.route('/top-ten')
def top_ten_books_sold():
    # TODO: Top ten books sold
    #    Sort by unitsSold decreasing
    booksQuery = Books.query.all()
    books: list = booksSchema.dump(booksQuery)
    sortedBooks = sorted(books, key=sortByUnitsSold, reverse=True)\

    # check size of sortedBooks.  If greater than 10, return only top ten, else return sorted books
    if len(sortedBooks) > 10:
        topTenBooks = []
        for idx in range(0, 10, 1):
            topTenBooks.append(sortedBooks[idx])
        return jsonify(topTenBooks)
    else:
        return jsonify(sortedBooks)


# UTILITY FUNCTIONS
def sortByUnitsSold(book: dict):
    return book["unitsSold"]
