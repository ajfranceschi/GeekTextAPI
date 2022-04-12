from flask import jsonify, abort
from core import db, marshmallow


class Users(db.Model):
    __tablename__ = 'Users'
    idUsers = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(45), nullable=False)
    passwordU = db.Column(db.String(45), nullable=False)
    emailAddress = db.Column(db.String(255), nullable=False)
    addressLine1 = db.Column(db.String(255), nullable=True)
    addressLine2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(45), nullable=True)
    state = db.Column(db.String(45), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)

    # Constructor
    def __init__(self, first_name, last_name, username, passwordU, emailAddress, addressLine1,
                 addressLine2, city, state,zipcode):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.passwordU = passwordU
        self.emailAddress = emailAddress
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def infoByUser(username):
        userQuery = Users.query.filter_by(username=username).one_or_none()
        if userQuery is not None:
            userSchema = UsersSchema(many=False)
            userReturned = userSchema.dump(userQuery)
            return userReturned
        else:
            abort(404, 'Username provided does not exist'.format(username=username))

    def createUser(first_name_1, last_name_1, user_name, password_U, email_Address, address_Line1,
                 address_Line2, city_1, state_1,zipcode_1):
        newUser = Users(first_name_1, last_name_1, user_name,
                         password_U, email_Address, address_Line1,
                         address_Line2, city_1, state_1, zipcode_1)
        db.session.add(newUser)
        db.session.commit()



# JSON Schema
class UsersSchema(marshmallow.Schema):

    class Meta:
        fields = ('idUsers', 'first_name', 'last_name', 'username', 'passwordU', 'emailAddress', 'addressLine1', 'addressLine2', 'city', 'state', 'zipcode')


User_schema = UsersSchema()
Users_schema = UsersSchema(many=True)


