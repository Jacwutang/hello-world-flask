from app import create_app
from db import db 
from user.query import create_user
import logging
logger = logging.getLogger(__name__)

app = create_app()

with app.app_context():
    logger.info("DB setup: drop and create")
    db.drop_all()
    db.create_all()
    create_user("admin", "password")
    logger.info("admin user created")


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)