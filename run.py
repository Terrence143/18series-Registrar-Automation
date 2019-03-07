from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class testAPI(Resource):
    def get(self):
        return {'welcome': "API Testing 2: Ok!"}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201


api.add_resource(testAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)
