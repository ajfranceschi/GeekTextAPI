from core import db, marshmallow
from datetime import datetime

# Authors table Model
class ShoppingCartItems(db.Model):
    __tablename__ = 'ShoppingCartItems'
    idShoppingCartItems = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idShoppingCarts = db.column(db.Integer,db.ForeignKey('ShoppingCarts.idShoppingCarts'),nullable = False)
    isbn = db.Column(db.String(55), nullable=False)


# JSON Schema
class ShoppingCartItemsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idShoppingCartItems', 'idShoppingCarts','isbn')


ShoppingCartItems_schema = ShoppingCartItemsSchema()
ShoppingCartItems_many_schema = ShoppingCartItemsSchema(many=True)