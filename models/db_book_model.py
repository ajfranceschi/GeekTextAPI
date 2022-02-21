from core import db, marshmallow


# Book model
class Books(db.Model):
    __tablename__ = 'Books'
    isbn = db.Column(db.Integer, primary_key=True, nullable=False)
    idAuthors = db.Column(db.Integer, db.ForeignKey('Authors.idAuthors'), nullable=False)
    bookTitle = db.Column(db.String(100), nullable=False)
    bookDescription = db.Column(db.Text, nullable=True)
    bookPrice = db.Column(db.Float, nullable=False)
    bookGenre = db.Column(db.String(80), nullable=False)
    bookPublisher = db.Column(db.String(255), nullable=False)
    bookYearPublished = db.Column(db.Integer, nullable=False)
    unitsSold = db.Column(db.Integer)
    bookRating = db.Column(db.Float)


class BooksSchema(marshmallow.Schema):
    class Meta:
        fields = ('isbn', 'idAuthors', 'bookTitle', 'bookDescription',
                  'bookPrice', 'bookGenre', 'bookPublisher', 'bookYearPublished',
                  'unitsSold', 'bookRating')


book_schema = BooksSchema()
books_schema = BooksSchema(many=True)

