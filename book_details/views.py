from flask import jsonify
from . import bookD_bp
from models.db_book_model import Books, books_schema


@bookD_bp.route('/')
def index():
    return "Books details Feature"


@bookD_bp.route('/getBookDetails')
def getBooks():
    books = Books.query.all()
    return jsonify(books_schema.dump(books))
