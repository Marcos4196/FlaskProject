#importing the flask class . An instance of this class will be
#the WSGI application
from flask import Flask, redirect, url_for ,request, render_template
from database import con
import sqlite3
from random import randint

#make a connection to database
con = sqlite3.connect('mydatabase.db', check_same_thread=False)
cur = con.cursor()

#creating an instance of the FLask Class
app = Flask(__name__)

#createunique user IDs
def unique_id():
    seed = 23  # Set your desired seed value
    while True:
        yield seed
        seed += 1
    

unique_sequence = unique_id()


#define the homepage
@app.route("/")
def home():
    return render_template("items.html", content="Passing this from backend")

@app.route("/login" , methods=["POST" , "GET"])
def login():
    
    #return render_template("formdata.html" ,  content=response )
    ## Return the extracted information  

@app.route("/users")
def display_users():
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    return render_template('showusers.html', usr=rows)


@app.route('/items')
def items():
    return render_template('items.html')

@app.route("/")
def user(usr):
    return render_template("user.html" , usr="user" , content=usr)


if __name__ =="__main__":
    app.run(host='0.0.0.0' , debug=True)
