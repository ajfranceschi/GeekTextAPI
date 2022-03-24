from core import db, marshmallow
from models.db_Shopping_Carts import ShoppingCarts


# ShoppingCartItem table Model
class ShoppingCartItems(db.Model):
    __tablename__ = 'ShoppingCartItems'
    idShoppingCartItems = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idShoppingCarts = db.Column(db.Integer, db.ForeignKey(ShoppingCarts.idShoppingCarts),
                                nullable = False)
    isbn = db.Column(db.String(55), nullable = False)


def __init__(self, id_shopping_carts, isbn):
    self.idShoppingCarts = id_shopping_carts
    self.isbn = isbn


def addItemToCart(isbn: str, idUsers: str ):
    cart = None
    # check for existence of cart
    try:
        cart = ShoppingCarts.query.filter_by(idUsers = idUsers).all()
    except Exception as e:
        print(e)
        return "Exception occurred", 500

    if len(cart) > 0:
        idShoppingCarts = cart[0].idShoppingCarts
        cart_item = ShoppingCartItems(idShoppingCarts = idShoppingCarts, isbn = isbn)

        try:
            db.session.add(cart_item)
            db.session.commit()
            result = ShoppingCartItems.query.filter_by(idShoppingCarts=idShoppingCarts)
            return ShoppingCartItems_many_schema.dump(result)
        except Exception as e:
            return e
    else:
        newCart = ShoppingCarts(idUsers=idUsers)
        try:
            db.session.add(newCart)
            db.session.commit()
            print(newCart.idShoppingCarts)
        except Exception as e:
            return e
        return "User does not have a cart"


def removeItemFromCart(isbn: str):
    item = ShoppingCartItems.query.filter_by(isbn=isbn).first()
    if item:
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            return e
        return "Item was remove from your shopping cart", 202


def getItems(idShoppingCarts: int ):
    try:
        items = ShoppingCartItems.query.filter_by(idShoppingCarts=idShoppingCarts).all()
    except Exception as e:
        return e
    return ShoppingCartItems_many_schema.dump(items)


# JSON Schema
class ShoppingCartItemsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idShoppingCartItems', 'idShoppingCarts', 'isbn')


ShoppingCartItems_schema = ShoppingCartItemsSchema()
ShoppingCartItems_many_schema = ShoppingCartItemsSchema(many = True)
