#importing the flask class . An instance of this class will be
#the WSGI application
from flask import Flask, redirect, url_for ,request, render_template, abort

#creating an instance of the FLask Class
app = Flask(__name__)



PRODUCTS = {
    'iphone':
    {
        'name':'Iphone 5s',
        'category':'phone',
        'price': 699
    },
    'galaxy':
    {
        'name':'Samsung galazy 5', 
        'category':'phones',
        'price':649
    },
    'ipad-air': 
    {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649,
    },
    'ipad-mini': {
        'name': 'iPad Mini',
        'category': 'Tablets',
        'price': 549
    }  
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@app.route('/product/<key>')
def product(key):
    product=PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html',product=product)
if __name__ =='__main__':
    app.run(host='0.0.0.0' , debug=True)