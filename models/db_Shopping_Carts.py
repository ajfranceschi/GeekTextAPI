from core import db, marshmallow


# Authors table Model
class ShoppingCarts(db.Model):
    __tablename__ = 'ShoppingCarts'
    idShoppingCarts = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idUsers = db.Column(db.Integer, db.ForeignKey("Users.idUsers"), nullable = False)


def __init__(self, idUsers):
    self.idUsers = idUsers


# JSON Schema
class ShoppingCartsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idShoppingCarts', 'idUsers')


ShoppingCart_schema = ShoppingCartsSchema()
ShoppingCarts_many_schema = ShoppingCartsSchema(many = True)
