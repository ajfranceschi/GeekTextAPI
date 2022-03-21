from flask import jsonify, request, flash
from flask_marshmallow import fields
from sqlalchemy import func, update, insert
from sqlalchemy.orm import query
from sqlalchemy.sql import Insert

from core import db
from . import comRate_bp
from models.db_Rating_Comments import RatingComments, ratingComments_many_schema, combineSchemas
from models.db_book_model import Books, booksSchema
from models.db_user_model import Users


# Main ratings and comments route
@comRate_bp.route('/')
def index():
    return "Ratings and Comments route"


# Returns all ratings and comments made by users
@comRate_bp.route('/returnAllRatings')
def returnAllRating():
    qry = db.session.query(RatingComments.ratingNumber, RatingComments.comments, RatingComments.createdAt, Users.username, Books.bookTitle) \
        .join(Users, RatingComments.idUsers == Users.idUsers).join(Books, RatingComments.isbn == Books.isbn).all()
    output = combineSchemas.dump(qry)
    return jsonify(output)


# Returns the highest rated comments of users from selected book
@comRate_bp.route('/returnBookHighestRating/<string:isbn>/')
def returnBookHighestRating(isbn):
    findMax = db.session.query(func.max(RatingComments.ratingNumber)).filter(RatingComments.isbn == isbn)
    qry = db.session.query(RatingComments.ratingNumber, RatingComments.comments, RatingComments.createdAt, Users.username, Books.bookTitle)\
        .join(Users, RatingComments.idUsers == Users.idUsers).join(Books, RatingComments.isbn == Books.isbn)\
        .filter(RatingComments.isbn == isbn, RatingComments.ratingNumber == findMax)
    output = combineSchemas.dump(qry)
    return jsonify(output)


# Returns the highest rated comments from users from the whole book collection
@comRate_bp.route('/returnAllHighestRating')
def returnAllHighestRating():
    findMax = db.session.query(func.max(RatingComments.ratingNumber))
    qry = db.session.query(RatingComments.ratingNumber, RatingComments.comments, RatingComments.createdAt, Users.username, Books.bookTitle)\
        .join(Users, RatingComments.idUsers == Users.idUsers).join(Books, RatingComments.isbn == Books.isbn)\
        .filter(RatingComments.ratingNumber == findMax)
    output = combineSchemas.dump(qry)
    return jsonify(output)


# Returns the average rating of a chosen book
@comRate_bp.route('/returnAverageBookRating/<string:isbn>/')
def returnAverageBookRating(isbn):
    avg = db.session.query(func.avg(RatingComments.ratingNumber)).filter(RatingComments.isbn == isbn).scalar() or 0
    qry = db.session.query(Books.bookTitle, Books.bookRating) \
        .filter(Books.isbn == isbn)
    if avg > 0:
        addAvg = update(Books).where(Books.isbn == isbn).\
            values(bookRating=avg)
    db.session.execute(addAvg)
    db.session.commit()

    output = booksSchema.dump(qry)
    return jsonify(output, "Average Rating:", avg)


# Returns the average rating of all books
@comRate_bp.route('/returnAllAverageBookRating')
def returnAllBookAverageRating():
    qry = db.session.query(Books.bookTitle, Books.bookRating)
    output = booksSchema.dump(qry)
    return jsonify(output)


@comRate_bp.route('/getAllComments')
def getAllComments():
    comments = RatingComments.query.all()
    return jsonify(ratingComments_many_schema.dump(comments))



















