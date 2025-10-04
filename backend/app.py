from flask import Flask, jsonify, request
from flask_cors import CORS
from routes import api
from models import db

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Routes configuration
api.init_app(app)

# @app.route('/')
# def home():
#     # return render_template('index.html') # in mad1
#     return {'message': 'Hello world!'} # in mad2

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)