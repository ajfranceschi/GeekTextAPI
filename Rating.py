import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0166143@ari',
    database='geek_text_db'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM Books')

Books = mycursor.fetchall()


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": Books})
