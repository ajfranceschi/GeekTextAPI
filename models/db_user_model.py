from core import db, marshmallow

class Users(db.Model):
    __tablename__ = 'Users'
    idUsers = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(45), nullable=False)
    emailAddress = db.Column(db.String(255), nullable=False)
    addressLine1 = db.Column(db.String(255), nullable=True)
    addressLine2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(45), nullable=True)
    state = db.Column(db.String(45), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)


# JSON Schema
class UsersSchema(marshmallow.Schema):
    class Meta:
        fields = ('idUsers', 'first_name', 'last_name', 'username', 'emailAddress', 'addressLine1', 'addressLine2', 'city', 'state', 'zipcode')


User_schema = UsersSchema()
Users_schema = UsersSchema(many=True)