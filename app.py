# This Python code snippet is setting up a Flask application with RESTful API endpoints for managing
# purchase orders and their items. Here's a breakdown of what each part does:
from flask import Flask
from flask_restful import Api

from purchase_orders.resources import PurchaseOrders

app = Flask(__name__)
api = Api(app)
def create_app():
    app = Flask(__name__)
    api = Api(app)
    

    
api.add_resource(PurchaseOrders, '/purchase_orders')
        
    
app.run(port=5000)