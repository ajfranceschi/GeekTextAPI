from flask import jsonify, abort

from core import db, marshmallow
from marshmallow import fields
from . import db_author_model


# Book model
class Books(db.Model):
    __tablename__ = 'Books'
    isbn = db.Column(db.String(55), primary_key=True, nullable=False)
    idAuthors = db.Column(db.Integer, db.ForeignKey('Authors.idAuthors'), nullable=False)
    bookTitle = db.Column(db.String(100), nullable=False)
    bookDescription = db.Column(db.Text, nullable=True)
    bookPrice = db.Column(db.Float, nullable=False)
    bookGenre = db.Column(db.String(80), nullable=False)
    bookPublisher = db.Column(db.String(255), nullable=False)
    bookYearPublished = db.Column(db.Integer, nullable=False)
    unitsSold = db.Column(db.Integer)
    bookRating = db.Column(db.Float)
    author = db.relationship('Authors', backref=db.backref('Authors', lazy='dynamic'))

    def __init__(self, isbn, idAuthors, bookTitle, bookDescription, bookPrice, bookGenre, bookPublisher,
                 bookYearPublished, unitsSold, bookRating):
        self.isbn = isbn
        self.idAuthors = idAuthors
        self.bookTitle = bookTitle
        self.bookDescription = bookDescription
        self.bookPrice = bookPrice
        self.bookGenre = bookGenre
        self.bookPublisher = bookPublisher
        self.bookYearPublished = bookYearPublished
        self.unitsSold = unitsSold
        self.bookRating = bookRating

    # Retrieve a book’s details by the ISBN
    def fetchABook(isbn):
        queryBook = Books.query.filter_by(isbn=isbn).one_or_none()
        if queryBook is not None:
            bookSchema = BooksSchema(many=False)
            bookReturned = bookSchema.dump(queryBook)
            return bookReturned
            # return jsonify(bookReturned)
        else:
            abort(404, 'Book not found for ID: {isbn}'.format(isbn=isbn))

    # Retrieve a list of books associate with an author
    def fetchListBooksByAuthor(idAuthor):
        queryBooks = Books.query.filter_by(idAuthors=idAuthor).all()
        if queryBooks:
            bookSchema = BooksSchema(many=True)
            booksReturned = bookSchema.dump(queryBooks)
            return booksReturned
        else:
            abort(404, 'Author not found for ID: {idAuthors}'.format(idAuthors=idAuthor))

    # Create a book with all the attributes
    def createBook(_isbn, _idAuthors, _bookTitle, _bookDescription, _bookPrice, _bookGenre, _bookPublisher,
                   _bookYearPublished, _unitsSold, _bookRating):
        new_book = Books(isbn=_isbn, idAuthors=_idAuthors, bookTitle=_bookTitle, bookDescription=_bookDescription,
                         bookPrice=_bookPrice, bookGenre=_bookGenre, bookPublisher=_bookPublisher,
                         bookYearPublished=_bookYearPublished,
                         unitsSold=_unitsSold, bookRating=_bookRating)
        db.session.add(new_book)
        db.session.commit()


class BooksSchema(marshmallow.Schema):
    isbn = fields.Str()
    idAuthors = fields.Int()
    bookTitle = fields.Str()
    bookDescription = fields.Str()
    bookPrice = fields.Number()
    bookGenre = fields.Str()
    bookPublisher = fields.Str()
    bookYearPublished = fields.Int()
    unitsSold = fields.Int()
    bookRating = fields.Number()
    author = fields.Nested(db_author_model.AuthorSchema)

    class Meta:
        fields = ('isbn', 'author', 'bookTitle', 'bookDescription',
                  'bookPrice', 'bookGenre', 'bookPublisher', 'bookYearPublished',
                  'unitsSold', 'bookRating')


varList = {'isbn', 'author', 'bookTitle', 'bookDescription', 'bookPrice', 'bookGenre', 'bookPublisher',
           'bookYearPublished', 'unitsSold', 'bookRating'}

bookSchema = BooksSchema()
booksSchema = BooksSchema(many=True)
