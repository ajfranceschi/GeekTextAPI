from core import db, marshmallow
from datetime import datetime


# Authors table Model
class ShoppingCart(db.Model):
    __tablename__ = 'ShoppingCart'
    idShoppingCart = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUser = db.Column(db.Integer, db.ForeignKey("Users.idUsers"), nullable=False)


def __init__(self, idShoppingCart, idUser):
    self.idShoppingCart = idShoppingCart
    self.idUser = idUser


# JSON Schema
class ShoppingCartSchema(marshmallow.Schema):
    class Meta:
        fields = ('idShoppingCart', 'idUser')


ShoppingCart_schema = ShoppingCartSchema()
ShoppingCart_many_schema = ShoppingCartSchema(many=True)