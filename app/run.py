from app import create_app
from db import db 
from user.model import User

app = create_app()

with app.app_context():
    db.create_all()

# Define the teardown function to delete all tables and records
@app.teardown_appcontext
def teardown_database(exception=None):
    db.drop_all()  # Drops all tables and deletes all records
    db.session.remove()  # Close the session to avoid leaks

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)