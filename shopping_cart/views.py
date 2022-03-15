from flask import jsonify,request
from . import cart_bp
from core import db
from models.db_Shopping_Carts import ShoppingCart, ShoppingCart_schema
from models.db_Shopping_Cart_Items import ShoppingCartItems, ShoppingCartItems_many_schema


@cart_bp.route('/')
def index():
    return "Shopping Cart route"


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
    bob_cart = ShoppingCart(idShoppingCart=1, idUser=000)
    db.session.add(bob_cart)
    book1 = ShoppingCartItems(idShoppingCartItems=1, idShoppingCart=1, isbn='1234567')
    db.session.add(book1)
    db.session.commit()


@cart_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    isbn=request.form['isbn']
    test= ShoppingCartItems.query.filter_by(isbn=isbn).first()
    if test:
        return jsonify(message='That Item is already in your shopping cart.'),409
    else:
        id_cart=request.form['idShoppingCart']
        id_items=request.form['idShoppingCartItems']
        cart_items=ShoppingCartItems(isbn=isbn, idShoppingCart=id_cart, idShoppingCartItems=id_items)
        db.session.add(cart_items)
        db.session.commit()
        return jsonify(message='Items was successfully add to the cart'),201


@cart_bp.route('/get_cart_items', methods=['GET'])
def get_cart_items():
    cart_items_query = ShoppingCartItems.query.all()
    cart_items_list = ShoppingCartItems_many_schema(cart_items_query)
    return jsonify(cart_items_list.data)

