from flask import Blueprint

# declare Author Blueprint (author_bp)
author_bp = Blueprint('author_bp', __name__, url_prefix = '/authors')

from . import views
