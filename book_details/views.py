from flask import jsonify, request, Response, make_response
from . import bookD_bp
from models.db_book_model import Books, booksSchema, varList, BooksSchema


@bookD_bp.route('/')
def index():
    return "Books details Feature"


@bookD_bp.route('/addBook', methods=['POST'])
def addBook():
    isbn = request.args.get('isbn')
    idAuthors = request.args.get('idAuthors')
    bookTitle = request.args.get('bookTitle')
    bookDescription = request.args.get('bookDescription')
    bookPrice = request.args.get('bookPrice')
    bookGenre = request.args.get('bookGenre')
    bookPublisher = request.args.get('bookPublisher')
    bookYearPublished = request.args.get('bookYearPublished')
    unitsSold = request.args.get('unitsSold')
    bookRating = request.args.get('bookRating')
    Books.createBook(isbn, idAuthors, bookTitle, bookDescription, bookPrice, bookGenre, bookPublisher,
                     bookYearPublished, unitsSold, bookRating)
    response = Response("New book added!", 200, mimetype='application/json')
    return response


@bookD_bp.route('/getABook/<string:isbn>/', methods=['GET'])
def getABook(isbn):
    queryBook = Books.query.filter_by(isbn=isbn).first()
    bookSchema = BooksSchema(many=True, only=varList)
    bookReturned = bookSchema.dump(queryBook)
    return jsonify(bookReturned)
