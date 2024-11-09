from flask import Blueprint
auth_routes = Blueprint('auth_routes', __name__, template_folder='templates')
from . import routes