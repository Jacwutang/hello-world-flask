from flask import Flask, session, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_session import Session
import redis

app = Flask(__name__)

# Configure the Flask app to use Redis for session management
app.config['SECRET_KEY'] = 'password'
app.config['SESSION_TYPE'] = 'redis'  # Use Redis to store session data
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True  # Sign the session cookie for security
app.config['SESSION_KEY_PREFIX'] = 'flask-session:'  # Prefix for session keys in Redis

# Connect to Redis server
app.config['SESSION_REDIS'] = redis.StrictRedis(host='redis', port=6379, db=0)

# Initialize the Flask-Session extension
Session(app)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)


# Create a sample user
user1 = User(1, "admin", "password")

# Define the user loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return user1

# Route to log in a user
@app.route('/login')
def login():
    login_user(user1)
   
    print("After login: ", dict(session))  # Print session data for debugging
    return (f"User {current_user.username} logged in")

# Route to show a basic message
@app.route('/')
def hello_world():
    return f"Current session data: {dict(session)}"

# Route to log out a user
@app.route('/logout')
@login_required
def logout():
    print("Before logout: ", dict(session))  # Debug session before logout
    logout_user()
    print("After logout: ", dict(session))  # Debug session after logout
    return redirect(url_for('login'))

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)