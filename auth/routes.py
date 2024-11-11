from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import request, current_app,  redirect, url_for, render_template
from user.query import find_user
from user.model import User
from db import db
from . import auth_routes


# Route to log in a user
@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = find_user(username, password)
        if user:
            print("FOUND USER:", user)
            #login_user(user)
            return (f"User {current_user.username} logged in")
        else:
            return redirect(url_for('auth_routes.login'))
    return render_template('login.html')

# Route to log out a user
@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_routes.login'))