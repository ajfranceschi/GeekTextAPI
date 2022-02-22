#from flask import jsonify
from . import cart_bp
#from models.db_Shopping_Carts import ShoppingCarts, ShoppingCarts_many_schema


@cart_bp.route('/')
def index():
    return "Shopping Cart route"


@cart_bp.route('/getCart')
def getCart():
    return {"Route": "Get Shopping Cart"}