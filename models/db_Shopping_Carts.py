from core import db, marshmallow


# Authors table Model
class ShoppingCarts(db.Model):
    __tablename__ = 'ShoppingCarts'
    idShoppingCarts = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idUsers = db.Column(db.Integer, db.ForeignKey("Users.idUsers"), nullable = False)


def __init__(self, idUsers):
    self.idUsers = idUsers


def newCart(idUsers: str):
    userCart = ShoppingCarts(isUsers=idUsers)
    if userCart:
        try:
            db.session.add(userCart)
            db.session.commit()
            return ShoppingCart_schema.dump(userCart)
        except Exception as e:
            return e
        return "Unable to create a cart for user", 202


# JSON Schema
class ShoppingCartsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idShoppingCarts', 'idUsers')


ShoppingCart_schema = ShoppingCartsSchema()
ShoppingCarts_many_schema = ShoppingCartsSchema(many = True)
