from flask import jsonify,request
from . import cart_bp
from models.db_Shopping_Carts import ShoppingCart, ShoppingCart_many_schema
from models.db_Shopping_Cart_Items import ShoppingCartItems, ShoppingCartItems_many_schema


@cart_bp.route('/')
def index():
    return "Shopping Cart route"


@cart_bp.route('/get_cart_items', methods=['GET'])
def get_cart_items():
    cart_items_query = ShoppingCartItems.query.all()
    cart_items_list = ShoppingCartItems_many_schema(cart_items_query)
    return jsonify(cart_items_list.data)

