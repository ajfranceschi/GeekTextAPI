from flask import Flask
from core.DB_CREDS import *

# initialize Flask
app = Flask(__name__)

# Configure Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
