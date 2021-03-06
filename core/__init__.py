# ===============================================================
# Created by: Antonio J. Franceschi
#
# This file contains application wide configurations such as Flask
# and SQLAlchemy instances.
# ===============================================================
from flask import Flask
from core.DB_CREDS import *
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# initialize Flask
app = Flask(__name__)

# TODO: Create a file named DB_CREDS.py in /Core/
#   Prior to connecting to DB, add the following to your /core/DB_CREDS.py file
#   1.  USERNAME = %your MySQL Server username%
#   2.  PASSWORD = %your MySQL Server password%
#   3.  HOST = 'localhost'
#   4.  PORT = '3306'
#   5.  DATABASE = 'geek_text_db'
# Configure Database connection
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
marshmallow = Marshmallow(app)

from book_browsing_sorting import bkBrowseSort_bp
from Rate_Com import comRate_bp
from shopping_cart import cart_bp
from profile_management import profman_bp
from book_details import bookD_bp
from authors import author_bp

app.register_blueprint(bkBrowseSort_bp)
app.register_blueprint(comRate_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(profman_bp)
app.register_blueprint(bookD_bp)
app.register_blueprint(author_bp)
