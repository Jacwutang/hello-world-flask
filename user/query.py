from .model import User
from db import db

def find_user(username, password):
    user = User.query.filter_by(username=username).first()
    
    if user and user.password == password:
        return user
    return None

def find_user_by_id(id):
    user = User.query.get(id)
    return user

def create_user(username, password):
    new_user = User(username=username, password=password)

    db.session.add(new_user)
    db.session.commit()
    



