from core import db, marshmallow


# WishLitItems model
class WishLitItems(db.Model):
    __tablename__ = 'WishLitItems'
    idWishListsItems = db.Column(db.Integer, primary_key = True, nullable = False)
    idWishLists = db.Column(db.Integer, db.ForeignKey('WishLists.idWishLists'), nullable = False)
    isbn = db.Column(db.String(55), db.ForeignKey('Books.isbn'), nullable = False)


class WishListItemsSchema(marshmallow.Schema):
    class Meta:
        fields = ('idWishListsItems', 'idWishLists', 'isbn')


wishListItem_schema = WishListItemsSchema()
wishListItems_schema = WishListItemsSchema(many = True)
