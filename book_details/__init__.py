from flask import Blueprint

# declare Book Details Blueprint (bookD_bp)
bookD_bp = Blueprint('bookD_bp', __name__, url_prefix = '/book-details')

from . import views
