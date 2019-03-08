from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

api = Api(app)

class testAPI(Resource):
    def get(self):
        return {'welcome': "API Testing 1: OK!"}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201


api.add_resource(testAPI, '/')

from boop import routes