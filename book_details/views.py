# ***************************************************************
# Author by: Carlos Gonzalez
#
# This file contains the routes for GeekText API
# Book Details
# ****************************************************************
from flask import jsonify, request, Response, abort
from . import bookD_bp
from models.db_book_model import Books, booksSchema, varList, BooksSchema


@bookD_bp.route('/')
def index():
    return "Books details Feature"


@bookD_bp.route('/addBook', methods=['POST'])
def addBook():
    try:
        isbn = str(request.args.get('isbn'))
        idAuthors = int(request.args.get('idAuthors'))
        bookTitle = str(request.args.get('bookTitle'))
        bookDescription = str(request.args.get('bookDescription'))
        bookPrice = float(request.args.get('bookPrice'))
        bookGenre = str(request.args.get('bookGenre'))
        bookPublisher = str(request.args.get('bookPublisher'))
        bookYearPublished = int(request.args.get('bookYearPublished'))
        unitsSold = int(request.args.get('unitsSold'))
        bookRating = float(request.args.get('bookRating'))

        Books.createBook(isbn, idAuthors, bookTitle, bookDescription, bookPrice, bookGenre, bookPublisher,
                         bookYearPublished, unitsSold, bookRating)
        response = Response("New book added!", 200, mimetype='application/json')
        return response
    except ValueError as e:
        print(e)
        return 'Params are not accurate.', 400


@bookD_bp.route('/getABook/', methods=['GET'])
def getABook():
    try:
        isbn = str(request.args.get('isbn'))
        returnBook = Books.fetchABook(isbn)
        if returnBook == 'QUERY_ERROR':
            return "Could not complete the request.", 500
        return jsonify(returnBook), 200
    except ValueError as e:
        print(e)
        return 'Params are not accurate.', 400


@bookD_bp.route('/getBooksByAuthor/', methods=['GET'])
def getBooksByAuthor():
    try:
        idAuthor = int(request.args.get('idAuthor'))
        returnBooks = Books.fetchListBooksByAuthor(idAuthor)
        if returnBooks == 'QUERY_ERROR':
            return "Could not complete the request.", 500
        return jsonify(returnBooks), 200
    except ValueError as e:
        print(e)
        return 'Params are not accurate.', 400
