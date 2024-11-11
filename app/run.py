from app import create_app
from db import db 
from user.query import create_user

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    create_user("admin", "password")

# Run the Flask app
if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5001, debug=True)