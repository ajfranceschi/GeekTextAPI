from flask import jsonify, request, Response
from . import profman_bp
from models.db_user_model import Users



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

@profman_bp.route('/getUserInfo/<string:username>/', methods=['GET'])
def getUserInfo(username):
    returnUser = Users.infoByUser(username)
    return jsonify(returnUser)

@profman_bp.route('/addUser', methods=['POST'])
def addUser():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    username = request.args.get('username')
    passwordU = request.args.get('passwordU')
    emailAddress = request.args.get('emailAddress')
    addressLine1 = request.args.get('addressLine1')
    addressLine2 = request.args.get('addressLine2')
    city = request.args.get('city')
    state = request.args.get('state')
    zipcode = request.args.get('zipcode')


    Users.createUser(first_name, last_name, username, passwordU, emailAddress, addressLine1, addressLine2, city, state, zipcode)
    response = Response("New User added!", 200, mimetype='application/json')
    return response