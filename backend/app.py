from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

# @app.route('/')
# def home():
#     # return render_template('index.html') # in mad1
#     return {'message': 'Hello world!'} # in mad2

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Bye world!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)