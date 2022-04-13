from flask import Blueprint

# declare Book Browsing and Sorting Blueprint (bbs_bp)
comRate_bp = Blueprint('comRate_bp', __name__, url_prefix = '/comments-ratings')

from . import views
