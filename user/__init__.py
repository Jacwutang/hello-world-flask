from flask import current_app, Blueprint, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


class User(UserMixin):
    def __init__(self,id,admin):
        self.id = id
        self.username = admin

user1 = User(1, "admin")