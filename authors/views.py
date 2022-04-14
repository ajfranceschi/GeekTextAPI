# ***************************************************************
# Author by: Carlos Gonzalez
#
# This file contains the routes for GeekText API
# Authors
# ****************************************************************
from flask import jsonify, request, Response, abort
from . import author_bp
from models.db_author_model import Authors, Authors_schema


@author_bp.route('/')
def index():
    return "Authors routes"


@author_bp.route('/addAuthor', methods = ['POST'])
def addAuthor():
    try:
        authorFirstName = str(request.args.get('authorFirstName'))
        authorLastName = str(request.args.get('authorLastName'))
        authorPublisher = str(request.args.get('authorPublisher'))
        authorBiography = str(request.args.get('authorBiography'))
        Authors.createAuthor(authorFirstName, authorLastName, authorPublisher, authorBiography)
        response = Response("New author added!", 200, mimetype = 'application/json')
        return response
    except ValueError as e:
        print(e)
        return 'Params are not accurate.', 400
