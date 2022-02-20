from flask import jsonify
from . import bkBrowseSort_bp
from models.db_book_model import Books, books_schema


@bkBrowseSort_bp.route('/')
def index():
    return "Books Browsing and Sorting root"


@bkBrowseSort_bp.route('/getbooks')
def getBooks():
    books = Books.query.all()
    return jsonify(books_schema.dump(books))
