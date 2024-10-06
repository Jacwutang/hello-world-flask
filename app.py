from flask import Flask, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user



app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

class User(UserMixin):
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
    
    @staticmethod
    def get(user_id):
        # Retrieve the user object from the in-memory store
        user_data = users.get(int(user_id))
        if user_data:
            return User(**user_data)
        return None




login_manager = LoginManager()
login_manager.init_app(app)

users = {
    1: {"id": 1, "username": "admin", "password": "password"}
}

user1 = User(1, "admin", "password")

@login_manager.user_loader
def load_user(user_id):
    return user1

@app.route('/login')
def login():
    login_user(user1)
    return "User logged in"


@app.route('/')
def hello_world():
    return 'Hello, my Moo Deng! One Change'


@app.route('/logout')
@login_required
def logout():
    print("LOGGED OUT")
    logout_user()
    return redirect(url_for('login'))
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)