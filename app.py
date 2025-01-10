# This Python code snippet is setting up a Flask application with RESTful API endpoints for managing
# purchase orders and their items. Here's a breakdown of what each part does:
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource

from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems 


app = Flask(__name__)
api = Api(app)


api.add_resource(PurchaseOrders, '/purchase_orders')  
api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

if __name__ == '__main__':
 app.run(port=5000)