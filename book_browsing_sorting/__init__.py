# ===============================================================
# Author: Antonio J. Franceschi & Carlos Gonzalez
#
# This file contains the Flask Blueprint for Book Browsing and Sorting
# feature
# ===============================================================
from flask import Blueprint

# declare Book Browsing and Sorting Blueprint (bbs_bp)
bkBrowseSort_bp = Blueprint('bkBrowseSort_bp', __name__, url_prefix = '/book-browsing-sorting')

from . import views
