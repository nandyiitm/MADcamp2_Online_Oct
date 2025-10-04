from flask import Flask, jsonify, request
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

users = []    

class UserRegister(Resource):
    def get(self):
        username = request.args.get('username')
        if not username:
            return {'message': 'Username is required'}, 400
        print(f"Registering user: {username}")
        users.append(username)
        return {'message': 'User registered successfully'}, 201
    
class UserLogin(Resource):
    def get(self):
        return {'message': 'User logged in successfully'}, 200
    
class UsersInfo(Resource):
    def get(self):
        return {'users': users}, 200

api.add_resource(HelloWorld, '/')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UsersInfo, '/users')

if __name__ == '__main__':
    app.run(debug=True)