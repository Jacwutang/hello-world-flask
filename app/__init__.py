from flask import Flask, session
from flask_session import Session
from flask_login import LoginManager
from auth import auth_routes
from user.query import find_user_by_id
from db import db
import redis
import os

def create_app():
    app = Flask(__name__)

    # #Register blueprints
    app.register_blueprint(auth_routes)

    #Initialize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return find_user_by_id(user_id)
    

    # Configure the Flask app to use Redis for session management
    app.config['SECRET_KEY'] = 'password'
    app.config['SESSION_TYPE'] = 'redis'  # Use Redis to store session data
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True  # Sign the session cookie for security
    app.config['SESSION_KEY_PREFIX'] = 'flask-session:'  # Prefix for session keys in Redis


    # Connect to Redis server
    if os.getenv("FLASK_ENV") != "development":
        app.config['SESSION_REDIS'] = redis.StrictRedis(host='session-cache-ab3pso.serverless.use1.cache.amazonaws.com', port=6379)
    else:
        app.config['SESSION_REDIS'] = redis.StrictRedis(host='redis', port=6379)
    # DB connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    
    db.init_app(app)

    # Initialize the Flask-Session extension
    Session(app)

    return app

