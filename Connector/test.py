# from Connector import UserService
from Connector import *
import time
# userService = UserService.UserService()
# userService.insert_user(User.User.user("OceanCT", "123"))
# user = userService.find_user_by_username("OceanCT")
# print(user.username,user.password)
service = ConnectingMessageService.ConnectingMessageService()
# service.insert_message(ConnectingMessage.Message(User.User.user("OceanCT"), "Hello World", []))
for k in service.fetch_message():
    print(k.message)