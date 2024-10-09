from flask import Flask, session
from flask_session import Session
import redis

def create_app():
    app = Flask(__name__)

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

