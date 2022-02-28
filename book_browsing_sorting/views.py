from flask import jsonify
from . import bkBrowseSort_bp
from models.db_book_model import Books, books_schema


# Root Book Browsing and Sorting endpoint: (*/book-browsing-sorting/)
@bkBrowseSort_bp.route('/')
def index():
    return "Books Browsing and Sorting root"


# Book Browsing and Sorting / Get All Books endpoint: (*/book-browsing-sorting/get-books)
@bkBrowseSort_bp.route('/get-books')
def getBooks():
    booksQuery = Books.query.all()
    books = books_schema.dump(booksQuery)
    for book in books:
        print(book)
    return jsonify(books_schema.dump(books))


# Book Browsing and Sorting / Get top 10 books sold endpoint: (*/book-browsing-sorting/top-ten-books-sold)
@bkBrowseSort_bp.route('/top-ten-books-sold')
def topTenBooksSold():
    # TODO: Top ten books sold
    #    Sort by unitsSold
    return "Top Ten Books Sold route"
