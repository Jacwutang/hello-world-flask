from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import current_app

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(current_app)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)


# # Route to log in a user
# @current_app.route('/login')
# def login():
#     login_user(user1)
   
#     print("After login: ", dict(session))  # Print session data for debugging
#     return (f"User {current_user.username} logged in")

# # Route to log out a user
# @current_app.route('/logout')
# @login_required
# def logout():
#     print("Before logout: ", dict(session))  # Debug session before logout
#     logout_user()
#     print("After logout: ", dict(session))  # Debug session after logout
#     return redirect(url_for('login'))