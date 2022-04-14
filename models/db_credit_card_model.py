from core import db, marshmallow
from models.db_user_model import Users


class Credit_Cards(db.Model):
    __tablename__ = 'UserCreditCards'
    idUserCreditCards = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idUsers = db.Column(db.Integer, nullable = True)
    creditCardNumber = db.Column(db.String(16), nullable = False)
    expirationMonth = db.Column(db.Integer, nullable = False)
    expirationYear = db.Column(db.Integer, nullable = False)
    securityCode = db.Column(db.Integer, nullable = False)
    billingStreetAddress = db.Column(db.String(255), nullable = False)
    billingCity = db.Column(db.String(255), nullable = False)
    billingState = db.Column(db.String(4), nullable = False)
    billingZipCode = db.Column(db.Integer, nullable = False)

    def __init__(self, idUsers, creditCardNumber, expirationMonth, expirationYear, securityCode,
                 billingStreetAddress, billingCity, billingState, billingZipCode):
        self.idUsers = idUsers
        self.creditCardNumber = creditCardNumber
        self.expirationYear = expirationYear
        self.expirationMonth = expirationMonth
        self.securityCode = securityCode
        self.billingStreetAddress = billingStreetAddress
        self.billingCity = billingCity
        self.billingState = billingState
        self.billingZipCode = billingZipCode

    def getCreditCardsFor(idUsers):
        query = Credit_Cards.query.filter_by(idUsers = idUsers).all()
        if len(query) > 0:
            return creditCards_schema.dump(query)
        return 1

    def addCreditCart(idUsers, creditCardNumber, expirationMonth, expirationYear, securityCode,
                      billingStreetAddress, billingCity, billingState, billingZipCode):
        # validate user exists:
        userQuery = Users.query.filter_by(idUsers = idUsers).all()
        if len(userQuery) > 0:
            # We have a user
            newCreditCard = Credit_Cards(idUsers, creditCardNumber, expirationMonth, expirationYear, securityCode,
                                         billingStreetAddress, billingCity, billingState, billingZipCode)

            try:
                db.session.add(newCreditCard)
                db.session.commit()
            except Exception as e:
                print(e)
                return 'cc not added'

            return 'cc added'
        else:
            return "no user found"


# JSON Schema
class CreditCardsSchema(marshmallow.Schema):
    class Meta:
        fields = (
                'idUserCreditCards', 'idUsers', 'creditCardNumber', 'expirationMonth', 'expirationYear', 'securityCode')


creditCard_schema = CreditCardsSchema()
creditCards_schema = CreditCardsSchema(many = True)
