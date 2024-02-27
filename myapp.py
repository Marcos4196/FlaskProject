#importing the flask class . An instance of this class will be
#the WSGI application
from flask import Flask, redirect, url_for ,request, render_template

#creating an instance of the FLask Class
app = Flask(__name__)


users = [
    {'id': 1 , 'name': 'john'},
    {'id': 2 , 'name': 'nick'},
    {'id': 3 , 'name': 'ben'}
]


@app.route('/')
def index():
    return 'Index Page'

@app.route('/home')
def home_page():
    return "Welcome Home"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



#the route() decorator to tell Flask] what URL should trigger out function.
@app.route('/user/<int:id>')
def get_user_id(id):
    #for user in users:
    
    for user in users:
        if user['id'] == id:
            return user['name']
     





if __name__ =='__main__':
    app.run(host='0.0.0.0' , debug=True)