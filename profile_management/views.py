from flask import jsonify, request, Response
from . import profman_bp
from models.db_user_model import Users
from models.db_credit_card_model import Credit_Cards
from core import db


@profman_bp.route('/')
def index():
    return "Profile Management route"


@profman_bp.route('/getProf')
def getProfile():
    return {"Route": "Get Profile Management"}


# @profman_bp.route('/getAll')
# def getUsers():
#     userQuery = Users.query.all()
#     allUsers = Users_schema.dump(userQuery)
#     return jsonify(allUsers), 200

@profman_bp.route('/getUserInfo/<string:username>/', methods = ['GET'])
def getUserInfo(username):
    returnUser = Users.infoByUser(username)
    if returnUser == 0:
        return {'Error': f'{username} was not found.'}, 400
    else:
        return jsonify(returnUser)


@profman_bp.route('/addUser', methods = ['POST'])
def addUser():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    passwordU = request.form['passwordU']
    emailAddress = request.form['emailAddress']
    addressLine1 = request.form['addressLine1']
    addressLine2 = request.form['addressLine2']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zipcode']

    Users.createUser(first_name, last_name, username, passwordU, emailAddress, addressLine1, addressLine2, city, state,
                     zipcode)
    response = Response("New User added!", 200, mimetype = 'application/json')
    return response


@profman_bp.route('/updateUser/<int:idUsers>', methods = ['GET', 'POST'])
def updateUser(idUsers):
    userQuery = Users.query.get_or_404(idUsers)

    if request.method == "POST":

        for key in request.form:
            if key != "emailAddress":
                setattr(userQuery, key, request.form[key])

        try:
            db.session.commit()
            return "Information successfully update", 200

        except Exception as e:
            return "Error! There was an error in the process", 500


@profman_bp.route('/add-credit-card', methods = ['POST'])
def addCreditCard():
    try:
        idUsers = int(request.form['userId'])
        creditCardNumber = int(request.form['creditCardNumber'])
        expirationMonth = int(request.form['expirationMonth'])
        expirationYear = int(request.form['expirationYear'])
        securityCode = int(request.form['securityCode'])
        billingStreetAddress = str(request.form['billingStreetAddress'])
        billingCity = str(request.form['billingCity']).title()
        billingState = str(request.form['billingState']).upper()
        billingZipCode = int(request.form['billingZipCode'])

        result = Credit_Cards.addCreditCart(idUsers, creditCardNumber, expirationMonth, expirationYear,
                                            securityCode,
                                            billingStreetAddress, billingCity, billingState, billingZipCode)
        if result == 'cc not added':
            return {'Error': 'There was an error adding your CC please try again later'}, 500
        elif result == 'cc added':
            return {'Success': 'Credit added and linked to user'}, 200
        elif result == 'no user found':
            return {'Error': f'No user found for userID {idUsers}'}, 400
        else:
            return {'Error': 'Please try again later.'}
    except Exception as e:
        print(e)
        return {'Error': 'Error adding credit card'}, 500


@profman_bp.route('/get-credit-cards', methods = ['GET'])
def getCreditCards():
    if len(request.args) > 0:
        try:
            idUsers = int(request.args['userId'])
            result = Credit_Cards.getCreditCardsFor(idUsers)
            if result == 1:
                return {'Error': f'No credit cards found for userId: {idUsers}'}
            creditCardList = {'UserID': idUsers, 'creditCards': result}
            return jsonify(creditCardList)
        except Exception as e:
            print(e)
            return {'Error': 'Please make sure the parameter \'userId\' <int> is sent with the request.'}, 400
    else:
        return {'Error': 'Please make sure the parameter \'userId\' <int> is sent with the request.'}, 400
