from flask import jsonify, request
from . import cart_bp
from core import db
from models.db_Shopping_Carts import ShoppingCarts, ShoppingCart_schema, ShoppingCarts_many_schema
from models.db_Shopping_Cart_Items import addItemToCart, ShoppingCartItems, ShoppingCartItemsSchema, \
    ShoppingCartItems_many_schema


@cart_bp.route('/')
def index():
    return "Shopping Cart route"


# Initialize the database, I did this to be able to check if the add_item function is working.
# It gives me that item already in your shopping if user put the same isbn
@cart_bp.cli.command('db_create')
def db_create():
    db.create_all
    print('Database Created!')


@cart_bp.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@cart_bp.cli.command('db_seed')
def db_seed():
    bob_cart = ShoppingCarts(idShoppingCart = 1, idUser = 000)
    db.session.add(bob_cart)
    book1 = ShoppingCartItems(idShoppingCartItems = 1, idShoppingCart = 1, isbn = '1234567')
    db.session.add(book1)
    db.session.commit()


# Created an Items object
@cart_bp.route('/add_item', methods = ['POST'])
def add_item():
    isbn = request.form['isbn']
    idUsers = request.form['idUsers']
    return jsonify(addItemToCart(isbn, idUsers))


@cart_bp.route('/remove_item/<string:isbn>', methods = ['DELETE'])
def remove_item(isbn: str):
    item = ShoppingCartItems.query.filter_by(isbn = isbn).first()
    if item:
        db.session.delete(item)
        db.session.commit()


@cart_bp.route('/get_cart_items', methods = ['GET'])
def get_cart_items():
    items = ShoppingCartItems.query.all()
    return jsonify(ShoppingCartItems_many_schema.dump(items))
