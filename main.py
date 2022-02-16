from flask import Flask, request, jsonify
from core import app


# Root API route http://localhost:81/
@app.route('/', methods=['GET'])
def root():
    return "This is the root route for GeekText"


# /get route to serve as an example of a GET request (http://localhost:81/get)
@app.route('/get', methods=['GET'])
def process_get():
    print(request.args.get)
    return jsonify({"hello": "You"})


# /post route to serve as an example of a GET request (http://localhost:81/post)
@app.route('/post', methods=['POST'])
def post():
    print(request.form)
    return jsonify({"hello": "You"})


# function that starts the Flask listener.  App will be listening on localhost:81
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug=True)
