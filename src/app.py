from flask import Flask, request, abort
from flask_restful import Resource, Api

from converter import Converter

app = Flask(__name__)
api = Api(app)

class ConverterResource(Resource):
    def get(self, number):
        output = ''
        try:
            converter = Converter()
            output = converter.translate(int(number))
        except Exception as error:
            abort(400, str(error))

        return {
            'input': number,
            'output': output
        }

api.add_resource(ConverterResource, '/<number>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
