from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import current_app, Blueprint, redirect, url_for
from user.model import test_user
#from app.run import db
from user.model import User
from db import db

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/')
def hello():
    return "Hellooo"

# Route to log in a user
@auth_routes.route('/login')
def login():
    login_user(test_user)
    return (f"User {current_user.username} logged in")

# # Route to log out a user
@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_routes.login'))