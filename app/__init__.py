from flask import Flask, session
from flask_session import Session
from flask_login import LoginManager
from auth import auth_routes
from user.query import find_user_by_id
from db import db
import redis
import os
import logging
import sys
import boto3
import json
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def get_db_credentials(secret_name, region_name="us-east-1"):
    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)
    
    try:
        # Get the secret value
        response = client.get_secret_value(SecretId=secret_name)
        print("aws response:", response)
        # Parse and return the secret
        if "SecretString" in response:
            secret = response["SecretString"]
            return json.loads(secret)
        else:
            raise ValueError("SecretString not found in response")
    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        raise e

secret_name = "rds!db-4d451755-c8f4-4cac-9b5e-3c349a03cccc"
credentials = get_db_credentials(secret_name)

def create_app():
    logger.info("Initializing App")

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


    # Connect to Redis server and DB connection
    if os.getenv("FLASK_ENV") != "development":
        app.config['SESSION_REDIS']  = redis.StrictRedis(host='redis-ab3pso.serverless.use1.cache.amazonaws.com', port=6379, ssl=True)
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{credentials['username']}:{credentials['password']}@mysql.c74suywgmlyf.us-east-1.rds.amazonaws.com:3306/mydatabase"
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:[H_%}6|3K_8es>ly_tdmMVX6uw|r@mysql.c74suywgmlyf.us-east-1.rds.amazonaws.com:3306/mydatabase'
    else:
        app.config['SESSION_REDIS'] = redis.StrictRedis(host='redis', port=6379)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@mysql:3306/mydatabase'
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    
    app.config['SQLALCHEMY_ECHO'] = True
    
    db.init_app(app)

    # Initialize the Flask-Session extension
    Session(app)

    logger.info("Successfully Initializing App")
    
    return app

