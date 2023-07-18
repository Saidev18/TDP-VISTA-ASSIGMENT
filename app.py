from flask import Flask
from api.movies import movies_api
from api.auth import auth_api
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(movies_api)
app.register_blueprint(auth_api)
load_dotenv()


if __name__ == '__main__':
    app.run()
