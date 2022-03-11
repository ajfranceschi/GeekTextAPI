from flask import jsonify
from . import bkBrowseSort_bp
from models.db_book_model import Books, books_schema
from models.db_author_model import Authors, Author_schema, Authors_schema


# Root Book Browsing and Sorting endpoint: (*/book-browsing-sorting/)
@bkBrowseSort_bp.route('/')
def index():
    return "Books Browsing and Sorting root"


# Book Browsing and Sorting / Get All Books endpoint: (*/book-browsing-sorting/get-books)
@bkBrowseSort_bp.route('/get-books')
def getBooks():
    booksQuery = Books.query.all()
    for book in booksQuery:
        print(book)
    booksList = books_schema.dump(booksQuery)
    return jsonify(booksList)


# Book Browsing and Sorting / Get top 10 books sold endpoint: (*/book-browsing-sorting/top-ten-books-sold)
@bkBrowseSort_bp.route('/top-ten-books-sold')
def topTenBooksSold():
    # TODO: Top ten books sold
    #    Sort by unitsSold decreasing
    return "Top Ten Books Sold route"

# UTILITY FUNCTIONS
