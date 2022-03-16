from core import db, marshmallow
from datetime import datetime


# Authors table Model
class ShoppingCartItems(db.Model):
    __tablename__ = 'ShoppingCartItems'
    idShoppingCartItems = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idShoppingCart = db.Column(db.Integer, db.ForeignKey('ShoppingCarts.idShoppingCarts'), nullable = False)
    isbn = db.Column(db.String(55), nullable = False)


def __init__(self, idShoopingCartItems, idShoppingCart, isbn):
    self.idShoppingCartItems = idShoopingCartItems
    self.idShoppingCart = idShoppingCart
    self.isbn = isbn


# JSON Schema
class ShoppingCartItemsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idShoppingCartItems', 'idShoppingCart', 'isbn')


ShoppingCartItems_schema = ShoppingCartItemsSchema()
ShoppingCartItems_many_schema = ShoppingCartItemsSchema(many = True)
