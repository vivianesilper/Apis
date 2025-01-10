# This Python code snippet is setting up a Flask application with RESTful API endpoints for managing
# purchase orders and their items. Here's a breakdown of what each part does:
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource



def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.run(port=5000)
    
    return app