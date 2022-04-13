from flask import Blueprint

# declare Book Browsing and Sorting Blueprint (bbs_bp)
cart_bp = Blueprint('cart_bp', __name__, url_prefix = '/shopping-carts')

from . import views
