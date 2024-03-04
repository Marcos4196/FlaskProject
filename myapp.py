#importing the flask class . An instance of this class will be
#the WSGI application
from flask import Flask, redirect, url_for ,request, render_template

#creating an instance of the FLask Class
app = Flask(__name__)


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
            response = "infosubmited"
        if request.form['submit_button'] == 'register':
            response = "registered"
    return render_template("formdata.html" ,  content=response )
    ## Return the extracted information  

@app.route('/items')
def items():
    return render_template('items.html')

@app.route("/user")
def user():
    return render_template("user.html")





if __name__ =="__main__":
    app.run(host='0.0.0.0' , debug=True)
