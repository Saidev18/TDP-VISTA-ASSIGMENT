from flask import Blueprint

movies_api = Blueprint('movies_api', __name__, url_prefix='/movies')
auth_api = Blueprint('auth_api', __name__, url_prefix='/auth')

from . import movies, auth
