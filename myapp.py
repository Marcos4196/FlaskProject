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

@app.route('/navpage') 
def navpage(): 
    return render_template('navpage.html')

@app.route('/read-form', methods=['POST']) 
def read_form(): 
  
    # Get the form data as Python ImmutableDict datatype  
    data = request.form 
    return render_template("formdata.html" ,  content=data )
    ## Return the extracted information  

@app.route('/items')
def items():
    return render_template('items.html')




@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ =="__main__":
    app.run(host='0.0.0.0' , debug=True)
