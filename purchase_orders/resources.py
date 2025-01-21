from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrderModel


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida'
        
    )
    
    def get(self):
        purchase_orders = PurchaseOrderModel.find_all()
        return [p.as_dict() for p in purchase_orders]
    
    def post(self,id):
        data = PurchaseOrders.parser.parse_args()
        
        purchase_order= PurchaseOrderModel(**data)
        purchase_order.save()
        
        purchase_order.as_dict()
        
        return purchase_order.as_dict()
class  PurchaseOrdersById(Resource): 
    def get(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message': 'Purchase order {} não encontrado'.format(id)})
