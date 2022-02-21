from flask import jsonify
from . import comRate_bp
from models.db_Rating_Comments import RatingComments, ratingComments_many_schema


@comRate_bp.route('/')
def index():
    return "Ratings and Comments route"


@comRate_bp.route('/getComments')
def getComments():
    return {"Route": "Get Comments Route"}


@comRate_bp.route('/getAllCommnets')
def getAllComments():
    comments = RatingComments.query.all()
    return jsonify(ratingComments_many_schema.dump(comments))
