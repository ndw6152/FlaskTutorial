from flask_restful import Resource, reqparse, abort

import wikiquotes


class HelloWorld(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('updated_values', type=dict, location='json')

    def get(self, author):
        quote = wikiquotes.random_quote(author, "english")
        result = quote + "\n" +author
        return result

    def put(self, author):
        pass

    def delete(self, author):
        pass