from flask import jsonify
from . import comRate_bp
from models.db_Rating_Comments import RatingsComments, ratingComments_many_schema


@comRate_bp.route('/')
def index():
    return "Ratings and Comments route"


@comRate_bp.route('/getComments')
def getComments():
    return {"Route": "Get Comments Route"}
