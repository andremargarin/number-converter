from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ConverterResource(Resource):
    def get(self):
        return {
            'input': 'not implemented',
            'output': 'not implemented'
        }

api.add_resource(ConverterResource, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
