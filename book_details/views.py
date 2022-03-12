from flask import jsonify
from . import bookD_bp
from models.db_book_model import Books, booksSchema


@bookD_bp.route('/')
def index():
    return "Books details Feature"


@bookD_bp.route('/getBookDetails')
def getBooks():
    books = Books.query.all()
    return jsonify(booksSchema.dump(books))
