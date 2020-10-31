import flask
from flask import request
import mysql.connector
import sys
import pymysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# an API running on the database machine to authenticate, handle incoming requests, and return appropriate responses


@app.route('/register_pet', methods = ['GET', 'POST'])
def chat():
    print("hello world")
    name = request.args.get('name')
    type = request.args.get('type')
    address = request.args.get('address')

    print("name :", name)
    print("type :", type)
    print("address :", address)

    select_query = "INSERT INTO pet (pet_name, pet_type, pet_address) VALUES (%s, %s, %s)"
    insert_values = (name, type, address)
    try:
        db_cursor.execute(select_query, insert_values)
        adopt_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"
# @app.route('/', methods = ['GET', 'POST'])
# def chat():

#     msg_subject = request.args.get('subject')

#     # msg_received = flask.request.get_json()
#     # msg_subject = msg_received["subject"]

#     if msg_subject == "register":
#         return register(msg_received)
#     elif msg_subject == "login":
#         return login(msg_received)
#     elif msg_subject == "register_pet":
#         return register_pet()
#     else:
#         return "Invalid request."

def register_pet():
    name = request.args.get('name')
    type = request.args.get('type')
    address = request.args.get('address')


    # name = msg_received["name"]
    # type = msg_received["type"]
    # address = msg_received["address"]
    print("name :", name)
    print("type :", type)
    print("address :", address)

    select_query = "INSERT INTO pet (pet_name, pet_type, pet_address) VALUES (%s, %s, %s)"
    insert_values = (name, type, address)
    try:
        db_cursor.execute(select_query, insert_values)
        chat_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"


def register(msg_received):
    firstname = msg_received["firstname"]
    lastname = msg_received["lastname"]
    email = msg_received["email"]
    password = msg_received["password"]

    select_query = "SELECT * FROM users where user_email = " + "'" + email + "'"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()
    if len(records) != 0:
        return "You have already signed up using this email. Please choose another email account."

    insert_query = "INSERT INTO users (user_first_name, user_last_name, user_email, user_pwd) VALUES (%s, %s, %s, MD5(%s))"
    insert_values = (firstname, lastname, username, password)
    try:
        db_cursor.execute(insert_query, insert_values)
        chat_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

def login(msg_received):
    email = msg_received["email"]
    password = msg_received["password"]
    select_query = "SELECT * FROM users where user_email = " + "'" + email + "'  and user_pwd = '" + password + "'"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        return "success"

try:
    adopt_db = pymysql.connect(host="localhost",user="root",passwd="Tszchun1126",database="adopt" )
except:
    sys.exit("Error connecting to the database. Please check your inputs.")

db_cursor = adopt_db.cursor()

app.run(host="0.0.0.0", port=5000, debug=True, threaded=True) # Run in development server.
# waitress.serve(app=app, host="0.0.0.0", port=5000) # Run in production server.