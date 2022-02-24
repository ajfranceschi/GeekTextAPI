from core import db, marshmallow


# WishLits model
class WishLits(db.Model):
    __tablename__ = 'WishLists'
    idWishLists = db.Column(db.Integer, primary_key=True, nullable=False)
    idUsers = db.Column(db.Integer, db.ForeignKey('Users.idUsers'), nullable=False)
    name = db.Column(db.String(45), nullable=False)


class WishListsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idWishLists', 'idUsers', 'name')


wishList_schema = WishListsSchema()
wishLists_schema = WishListsSchema(many=True)

