from datetime import datetime
from flask import jsonify, request
from sqlalchemy import func, update
from core import db
from . import comRate_bp
from models.db_Rating_Comments import RatingComments, combineSchemas
from models.db_book_model import Books, booksSchema
from models.db_user_model import Users


# Main ratings and comments route
@comRate_bp.route('/')
def index():
    return "Ratings and Comments route"


# Returns the highest rated comments from selected book
@comRate_bp.route('/returnBookHighestRating/<string:isbn>/')
def returnBookHighestRating(isbn):
    findMax = db.session.query(func.max(RatingComments.ratingNumber)).filter(RatingComments.isbn == isbn)
    qry = db.session.query(RatingComments.ratingNumber, RatingComments.comments, RatingComments.createdAt, Users.username, Books.bookTitle)\
        .join(Users, RatingComments.idUsers == Users.idUsers).join(Books, RatingComments.isbn == Books.isbn)\
        .filter(RatingComments.isbn == isbn, RatingComments.ratingNumber == findMax)
    output = combineSchemas.dump(qry)
    return jsonify(output)


# Returns the highest rated comments from the whole book collection
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
    oldAvg = db.session.query(RatingComments.ratingNumber).filter(RatingComments.isbn == isbn)
    avg = db.session.query(func.avg(RatingComments.ratingNumber)).filter(RatingComments.isbn == isbn).scalar() or 0
    qry = db.session.query(Books.bookTitle, Books.bookRating) \
        .filter(Books.isbn == isbn)
    # checks that the average rating already in database is different from the newly found average
    if avg != oldAvg:
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


# Allows user to add a rating and comment for chosen book
@comRate_bp.route('/addCommentRating/<string:isbn>/<string:username>', methods=['POST'])
def addCommentRating(isbn, username):
    idUserExists = db.session.query(db.exists().where(Users.username == username)).scalar()
    # checks if user exists before adding comment/rating
    if idUserExists:
        idUsers = db.session.query(Users.idUsers).filter(Users.username == username)
        checkUserStatus = db.session.query(RatingComments).filter(RatingComments.idUsers == idUsers, RatingComments.isbn == isbn).count()
        # checks if user has already left a review for specific book
        if checkUserStatus == 0:
            ratingNumber = request.form['ratingNumber']
            title = request.form['title']
            comments = request.form['comments']
            # checks that the rating number does not exceed 5
            if ratingNumber > '5':
                return 'Rating number must be less than 5.'
            createdAt = datetime.utcnow()
            modifiedAt = datetime.utcnow()
            status = 0
            RatingComments.addComment(ratingNumber, comments, title, isbn, idUsers, createdAt, modifiedAt, status)
            return 'Comment added.'
        else:
            return 'User already left review for this book.'
    else:
        return 'User does not exist. Must login or create account.', 404
