from flask import Blueprint

profman_bp = Blueprint('profman_bp', __name__, url_prefix = '/profile-management')

from . import views
