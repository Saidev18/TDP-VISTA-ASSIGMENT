from flask import jsonify, request
from . import auth_api
from models.user import User
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')

valid_api_keys = ['9f63bab9']  # Add your valid API keys here

@auth.verify_token
def verify_token(token):
    if token in valid_api_keys:
        return token
    return None

@auth_api.route('/login', methods=['POST'])
@auth.login_required
def login():
    return jsonify({'message': 'Login successful'}), 200

