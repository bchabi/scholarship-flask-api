from flask import Flask, request
from flask_restful import Resource, Api
from searchquery import *


app = Flask(__name__)
api = Api(app)


class Scholarships(Resource):
    """This class takes in a query request argument q GET request and returns the result of the searchQuery function"""
    def get(self):
        args = request.args['q'].lower()
        return searchQuery(args)

api.add_resource(Scholarships, '/scholarships')

if __name__ == "__main__":
    app.run(port=8000, debug = True)