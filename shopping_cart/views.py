from flask import jsonify, request
from . import cart_bp
from models.db_Shopping_Cart_Items import *


@cart_bp.route('/')
def index():
    return "Shopping Cart route"


# Created an Items object
@cart_bp.route('/add_item', methods = ['POST'])
def add_item():
    isbn = request.form['isbn']
    idUsers = request.form['idUsers']
    return jsonify(addItemToCart(isbn, idUsers))


@cart_bp.route('/remove_item/<string:isbn>', methods = ['DELETE'])
def remove_item(isbn: str):
    isbn = request.form['isbn']
    return jsonify(removeItemFromCart(isbn))


@cart_bp.route('/get_cart_items', methods = ['GET'])
def get_cart_items():
    idShoppingCarts = request.form['idShoppingCarts']
    return jsonify(getItems())
