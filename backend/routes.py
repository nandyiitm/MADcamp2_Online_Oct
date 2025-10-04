from flask_restful import Api, Resource
from flask import request
api = Api()

from models import User, Post, db

## Authentication related routes

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        # validation of input data
        if not data or 'username' not in data or 'password' not in data:
            return {'message': 'Username and password required'}, 400
        if not data['username'] or not data['password']:
            return {'message': 'Username and password cannot be empty'}, 400
        
        # add user to database
        username = data['username']
        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400
        new_user = User(username=username, password=data['password'])
        db.session.add(new_user); db.session.commit()
        return {'message': 'User registered successfully', 'id': new_user.id}, 201
api.add_resource(UserRegister, '/register')

class UserLogin(Resource):
    def get(self):
        return {'message': 'User logged in successfully'}, 200
api.add_resource(UserLogin, '/login')

## Admin related routes
   
# class UsersInfo(Resource):
#     def get(self):
#         return {'users': users}, 200
# api.add_resource(UsersInfo, '/users')

## User related routes

class Posts(Resource):
    def get(self, id=None):
        if id:
            post = Post.query.get(id)
            if not post:
                return {'message': 'Post not found'}, 404
            post = {'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id}
            return {'post': post}, 200
        posts = Post.query.all()
        posts = [{'id': p.id, 'title': p.title, 'content': p.content, 'user_id': p.user_id} for p in posts]
        return {'posts': posts, 'message': 'All posts'}, 200

    def post(self):
        data = request.get_json()
        if not data or 'title' not in data or 'content' not in data:
            return {'message': 'Title, content, and user_id are required'}, 400
        if not data['title'] or not data['content'] or 'user_id' not in data or not data['user_id']:
            return {'message': 'Title, content, and user_id cannot be empty'}, 400
        
        new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_post); db.session.commit()
        return {'message': 'Post created successfully'}, 201
    
    def put(self, id):
        data = request.get_json()
        if not data or 'title' not in data or 'content' not in data:
            return {'message': 'Title and content are required'}, 400
        if not data['title'] or not data['content']:
            return {'message': 'Title and content cannot be empty'}, 400
        post = Post.query.get(id)
        if not post:
            return {'message': 'Post not found'}, 404
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return {'message': 'Post updated successfully'}, 200
    
    def delete(self, id):
        post = Post.query.get(id)
        if not post:
            return {'message': 'Post not found'}, 404
        db.session.delete(post)
        db.session.commit()
        return {'message': 'Post deleted successfully'}, 200

api.add_resource(Posts, '/posts', '/posts/<int:id>')


