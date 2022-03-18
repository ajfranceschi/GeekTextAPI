from flask import jsonify, request, Response, abort
from . import author_bp
from models.db_author_model import Authors, Authors_schema

@author_bp.route('/')
def index():
    return "Authors routes"


@author_bp.route('/addAuthor', methods=['POST'])
def addAuthor():
    authorFirstName = request.args.get('authorFirstName')
    authorLastName = request.args.get('authorLastName')
    authorPublisher = request.args.get('authorPublisher')
    authorBiography = request.args.get('authorBiography')
    Authors.createAuthor(authorFirstName, authorLastName, authorPublisher, authorBiography)
    response = Response("New author added!", 200, mimetype='application/json')
    return response