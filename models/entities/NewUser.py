from werkzeug.security import generate_password_hash


class NewUser():

    def __init__(self, email, password, username,
                 name, lastname) -> None:
        self.email = email
        self.password = password
        self.username = username
        self.name = name
        self.lastname = lastname

    @classmethod
    def save_password(self, password):
        return generate_password_hash(password)
