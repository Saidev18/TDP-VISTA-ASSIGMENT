from flask import jsonify, request, current_app
from . import movies_api
import requests


@movies_api.route('/<movie_name>')
def get_movie_details(movie_name):
    api_key = current_app.config.get('API_KEY')
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={movie_name}'

    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return jsonify(movie_data)
    else:
        return jsonify({'error': 'Movie not found'}), 404


@movies_api.route('/')
def get_movie_list():
    api_key = current_app.config.get('API_KEY')
    url = f'http://www.omdbapi.com/?apikey={api_key}&s=*&type=movie'

    response = requests.get(url)
    if response.status_code == 200:
        movie_list = response.json()
        return jsonify(movie_list)
    else:
        return jsonify({'error': 'Failed to fetch movie list'}), 500
