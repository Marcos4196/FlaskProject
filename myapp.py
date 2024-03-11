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
    if request.method == "POST":
        user = request.form["email"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route('/read-form', methods=['POST']) 
def read_form(): 
  
    # Get the form data as Python ImmutableDict datatype  
    data = request.form 
    response = ""
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit':
            data = request.form
            #con = sqlite3.connect('mydatabase.db')
            #cur = con.cursor()
            cur.execute("SELECT 1 FROM users WHERE email = ? ", (data["userEmail"],))
            result = cur.fetchone()
            if result != data["userEmail"]:
                return render_template("formdata.html" ,  content="User does not exist" )

            
            return render_template("formdata.html" ,  content=data['userEmail'] )
        if request.form['submit_button'] == 'register':
            data = request.form
            #con = sqlite3.connect('mydatabase.db')
            ascii_values = [ord(c) for c in data["userEmail"]]
            
            id = randint(1,999) + sum(ascii_values)
            cur.execute("INSERT INTO USERS VALUES(?,?,?)", (id, data["userEmail"] , data["userPassword"]))
            con.commit()
            
            return render_template("user.html" ,  content=data["userEmail"] )
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

@app.route("/user")
def user():
    return render_template("user.html" , content="test")





if __name__ =="__main__":
    app.run(host='0.0.0.0' , debug=True)
