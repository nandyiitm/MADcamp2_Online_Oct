from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import api
from models import db, User

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Routes configuration
app.config['JWT_SECRET_KEY'] = 'this is a secret key'  # Change this to a random secret key
JWTManager(app)
api.init_app(app)

# @app.route('/')
# def home():
#     # return render_template('index.html') # in mad1
#     return {'message': 'Hello world!'} # in mad2

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', password='admin', role='admin')
            db.session.add(admin)
            db.session.commit()
            print('Admin user created with username "admin" and password "admin"')
    app.run(debug=True)