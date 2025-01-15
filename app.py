# This Python code snippet is setting up a Flask application with RESTful API endpoints for managing
# purchase orders and their items. Here's a breakdown of what each part does:
from flask import Flask
from flask import jsonify
from flask_restful import Api

from purchase_orders.resources import PurchaseOrders



def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    api.add_resource(PurchaseOrders, '/purchase_orders')

    
    return app