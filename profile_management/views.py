from flask import jsonify, request, Response, flash
from . import profman_bp
from models.db_user_model import Users
from core import db


@profman_bp.route('/')
def index():
    return "Profile Management route"


@profman_bp.route('/getProf')
def getProfile():
    return {"Route": "Get Profile Management"}


@profman_bp.route('/getUserInfo/<string:username>/', methods=['GET'])
def getUserInfo(username):
    returnUser = Users.infoByUser(username)
    return jsonify(returnUser)


@profman_bp.route('/addUser', methods=['POST'])
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
    response = Response("New User added!", 200, mimetype='application/json')
    return response


@profman_bp.route('/updateUser/<int:idUsers>', methods=['GET', 'POST'])
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
