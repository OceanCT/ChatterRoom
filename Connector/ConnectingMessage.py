import time
import json
from Connector import User


class Message:
    def __init__(self, user=User.User.user(), message="", receiver_id=list):
        self.user = user
        self.message = message
        self.receiver_id = receiver_id
        self.message_time = time.time()

    def to_dict(self):
        return {
            "message": self.message,
            "receiver_id": self.receiver_id,
            "user": self.user.to_dict()
        }

    @classmethod
    def dict_to_object(cls, message_dict: dict):
        return cls(User.User.dict_to_object(message_dict['user']), message_dict['message'], message_dict['receiver_id'])
