from core import db, marshmallow
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime


# Authors table Model
class RatingsComments(db.Model):
    __tablename__ = 'RatingsComments'
    idRatingComments = db.Column(db.Integer, db.ForeignKey("Books.isbn"), primary_key=True, autoincrement=True, nullable=False)
    isbn = db.Column(db.String(55), nullable=False)
    idUsers = db.Column(db.Integer, db.ForeignKey("Users.idUsers"), nullable=False)
    ratingNumber = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    comments = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    modifiedAt = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(TINYINT, nullable=False)


# JSON Schema
class RatingsCommentsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idRatingComments', 'isbn', 'idUsers', 'ratingNumber', 'title', 'comments', 'createdAt', 'modifiedAt', 'status')


ratingComments_schema = RatingsCommentsSchema()
ratingComments_many_schema = RatingsCommentsSchema(many=True)

