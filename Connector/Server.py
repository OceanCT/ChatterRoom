import json
import queue
import socket
import threading
import time
from Connector import ConnectingMessage
from Connector import UserService
from Connector import User
from Connector import ConnectingMessageService


class Server:
    listener_ip = '127.0.0.1'
    listener_port = 13875
    Buf = 102400
    message_in = queue.Queue()
    message_out = queue.Queue()
    caddr_list = []
    caddr_queue_for_add = queue.Queue()
    caddr_queue_for_delete = queue.Queue()
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    userService = UserService.UserService()

    def __init__(self):
        self.ss.bind((self.listener_ip, self.listener_port))
        self.ss.listen(20)
        threading.Thread(target=self.caddr_process).start()
        threading.Thread(target=self.storing_message).start()
        threading.Thread(target=self.sending_message).start()
        threading.Thread(target=self.ss_listen).start()

    def ss_listen(self):
        while True:
            cs, caddr = self.ss.accept()
            threading.Thread(target=self.cs_listen, args=(cs, caddr)).start()

    def cs_listen(self, cs, caddr):
        while True:
            data = cs.recv(self.Buf).decode('utf-8')
            if not data:
                break
            data = json.loads(data)
            print(data)
            data = ConnectingMessage.Message.dict_to_object(data)
            print(data.receiver_id)
            if data.message == 'login' or data.message == 'signup':
                res = ConnectingMessage.Message()
                if data.message == 'login':
                    res = self.login(data)
                elif data.message == 'signup':
                    res = self.signup(data)
                cs.sendall(bytes(json.dumps(res.to_dict()), 'utf-8'))
                if res.message == 'success':
                    caddr = (caddr[0], data.receiver_id[0])
                    print(caddr)
                    service = ConnectingMessageService.ConnectingMessageService()
                    for msg in service.fetch_message():
                        time.sleep(0.00000001)
                        self.send_message(caddr, msg)
                        print(msg.to_dict())
                    self.caddr_queue_for_add.put(caddr)
            else:
                data.message_time = time.time()
                self.message_in.put(data)
        cs.close()

    def __del__(self):
        self.ss.close()

    def login(self, msg: ConnectingMessage.Message):
        user = self.userService.find_user_by_username(msg.user.username)
        if not user.username:
            return ConnectingMessage.Message(user, "userNotExist", [])
        if user.username == msg.user.username and user.password == msg.user.password:
            return ConnectingMessage.Message(user, "success", [])
        else:
            return ConnectingMessage.Message(User.User.user(), "wrongPassword", [])

    def signup(self, msg: ConnectingMessage):
        user = self.userService.find_user_by_username(msg.user.username)
        if user.username:
            return ConnectingMessage.Message(user, "userHasExist", [])
        self.userService.insert_user(msg.user)
        return ConnectingMessage.Message(user, "success", [])

    def caddr_process(self):
        while True:
            while not self.caddr_queue_for_delete.empty():
                self.caddr_list.remove(self.caddr_queue_for_delete.get())
            self.caddr_list.append(self.caddr_queue_for_add.get())

    def storing_message(self):
        service = ConnectingMessageService.ConnectingMessageService()
        while True:
            message = self.message_in.get()
            service.insert_message(message)
            self.message_out.put(message)

    def sending_message(self):
        while True:
            message = self.message_out.get()
            message.user.password = ""
            for caddr in self.caddr_list.copy():
                print("caddr:", caddr)
                self.send_message(caddr, message)

    def send_message(self, caddr, msg):
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        try:
            cs.connect(caddr)
        except Exception as e:
            print(e)
            self.caddr_queue_for_delete.put(caddr)
        msg.receiver_id = []
        print(msg.to_dict())
        try:
            cs.sendall(bytes(json.dumps(msg.to_dict()), 'utf-8'))
        except Exception as e:
            print("Error happened when sending data to the client.")
            print(e)
        cs.close()
