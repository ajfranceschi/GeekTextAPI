from flask import jsonify
from . import comRate_bp
from models.db_Rating_Comments import RatingComments, ratingComments_many_schema, RatingsCommentsSchema, varlist


@comRate_bp.route('/')
def index():
    return "Ratings and Comments route"


@comRate_bp.route('/getComments')
def getComments():
    return {"Route": "Get Comments Route"}


@comRate_bp.route('/getAllComments')
def getAllComments():
    comments = RatingComments.query.all()
    return jsonify(ratingComments_many_schema.dump(comments))


@comRate_bp.route('/returnAllRatings')
def returnAllRating():
    rating = RatingComments.query.all()
    ratingsCommentsSchema = RatingsCommentsSchema (many=True, only=varlist)
    output = ratingsCommentsSchema.dump(rating)
    return jsonify(output)

@comRate_bp.route('/returnBookRating/<string:isbn>/')
def returnBookRating(isbn):
    rating = RatingComments.query.filter_by(isbn=isbn).all()
    ratingsCommentsSchema = RatingsCommentsSchema (many=True, only=varlist)
    output = ratingsCommentsSchema.dump(rating)
    return jsonify(output)

# returnBookRating/9780567830572
