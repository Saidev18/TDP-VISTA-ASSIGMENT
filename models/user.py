from werkzeug.security import generate_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

