from flask import Flask, session
from flask_session import Session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from auth.routes import auth_routes
from user import user1
import redis

def create_app():
    app = Flask(__name__)

    # #Register blueprints
    app.register_blueprint(auth_routes)

    # Initialize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return user1
    

    # Configure the Flask app to use Redis for session management
    app.config['SECRET_KEY'] = 'password'
    app.config['SESSION_TYPE'] = 'redis'  # Use Redis to store session data
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True  # Sign the session cookie for security
    app.config['SESSION_KEY_PREFIX'] = 'flask-session:'  # Prefix for session keys in Redis

    # Connect to Redis server
    app.config['SESSION_REDIS'] = redis.StrictRedis(host='redis', port=6379)

    # Initialize the Flask-Session extension
    Session(app)

    return app

