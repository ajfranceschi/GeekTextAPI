from core import db, marshmallow
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime

from models.db_book_model import BooksSchema
from models.db_user_model import UsersSchema


class RatingComments(db.Model):
    __tablename__ = 'RatingComments'
    idRatingComments = db.Column(db.Integer, db.ForeignKey("Books.isbn"), primary_key = True, autoincrement = True,
                                 nullable = False)
    isbn = db.Column(db.String(55), nullable = False)
    idUsers = db.Column(db.Integer, db.ForeignKey("Users.idUsers"), nullable = False)
    ratingNumber = db.Column(db.Float, nullable = False)
    title = db.Column(db.String(255), nullable = False)
    comments = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    modifiedAt = db.Column(db.DateTime, default = datetime.utcnow())
    status = db.Column(TINYINT, nullable = False)

    def __init__(self, ratingNumber, comments, title, isbn, idUsers, createdAt, modifiedAt, status):
        self.isbn = isbn
        self.idUsers = idUsers
        self.ratingNumber = ratingNumber
        self.comments = comments
        self.title = title
        self.createdAt = createdAt
        self.modifiedAt = modifiedAt
        self.status = status

    def addComment(EnterratingNumber, Entercomments, Entertitle, Enterisbn, EnteridUsers, EntercreatedAt,
                   EntermodifiedAt, Enterstatus):
        addNewComment = RatingComments(EnterratingNumber, Entercomments, Entertitle, Enterisbn, EnteridUsers,
                                       EntercreatedAt, EntermodifiedAt, Enterstatus)
        db.session.add(addNewComment)
        db.session.commit()


class RatingsCommentsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idRatingComments', 'isbn', 'idUsers', 'ratingNumber', 'title', 'comments',
                  'createdAt', 'modifiedAt', 'status')


class CombineSchemas(marshmallow.Schema):
    class Meta:
        data = UsersSchema
        bookdata = BooksSchema
        fields = ('bookTitle', 'ratingNumber', 'title', 'comments', 'createdAt', 'username')


ratingComments_schema = RatingsCommentsSchema()
ratingComments_many_schema = RatingsCommentsSchema(many = True)
combineSchemas = CombineSchemas(many = True)
