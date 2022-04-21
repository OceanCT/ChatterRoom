import pymysql


class User:
    def __init__(self,username="", password=""):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

    @classmethod
    def user(cls, username="", password=""):
        return cls(username, password)

    @classmethod
    def dict_to_object(cls, user_dict: dict):
        return User.user(user_dict['username'], user_dict['password'])


