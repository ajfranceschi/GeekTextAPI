from importlib.resources import Resource

from core import db, marshmallow
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime

from models.db_book_model import BooksSchema
from models.db_user_model import UsersSchema


class RatingComments(db.Model):
    __tablename__ = 'RatingComments'
    idRatingComments = db.Column(db.Integer, db.ForeignKey("Books.isbn"), primary_key=True, autoincrement=True,
                                 nullable=False)
    isbn = db.Column(db.String(55), nullable=False)
    idUsers = db.Column(db.Integer, db.ForeignKey("Users.idUsers"), nullable=False)
    ratingNumber = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    comments = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    modifiedAt = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(TINYINT, nullable=False)


class RatingsCommentsSchema(marshmallow.Schema):
    class Meta:
        fields = (
        'idRatingComments', 'isbn', 'idUsers', 'ratingNumber', 'title', 'comments', 'createdAt', 'modifiedAt', 'status')


class CombineSchemas(marshmallow.Schema):
    class Meta:
        data = UsersSchema
        bookdata = BooksSchema
        fields = ('bookTitle', 'ratingNumber', 'comments', 'createdAt', 'username')


class PostSchema(marshmallow.Schema):
    class Meta:
        model = RatingComments
        fields = ('idUsers', 'ratingNumber', 'comments')


ratingComments_schema = RatingsCommentsSchema()
ratingComments_many_schema = RatingsCommentsSchema(many=True)
combineSchemas = CombineSchemas(many=True)
postSchema = PostSchema(many=True)