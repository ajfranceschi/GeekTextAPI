from core import db, marshmallow


class Credit_Cards(db.Model):
    __tablename__ = 'UserCreditCards'
    idUserCreditCards = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idUsers = db.Column(db.Integer, nullable = True)
    creditCardNumber = db.Column(db.String(16), nullable = False)
    expirationDate = db.Column(db.String(7), nullable = False)
    securityCode = db.Column(db.Integer, nullable = True)


# JSON Schema
class UsersSchema(marshmallow.Schema):
    class Meta:
        fields = ('idUserCreditCards', 'idUsers', 'creditCardNumber', 'expirationDate', 'securityCode')


User_schema = UsersSchema()
Users_schema = UsersSchema(many = True)
