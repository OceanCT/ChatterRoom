import queue
import socket
import json
import threading
import time
from Connector import ConnectingMessage
from Connector import User
from tkinter import messagebox


class Client:
    user = User.User()
    server_ip = '127.0.0.1'
    server_port = 13875
    Buf = 102400
    error_message = ""
    listener_ip = '127.0.0.1'
    listener_port = 13876
    message_queue = queue.Queue()
    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    def __init__(self):
        self.receiver.bind((self.listener_ip, self.listener_port))
        self.receiver.listen(1)
        threading.Thread(target=self.receive_message).start()

    def send_message(self, data: str, receiver_id=list):
        receiver_id = ['all']
        msg = ConnectingMessage.Message(self.user, data, receiver_id)
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        try:
            cs.connect((self.server_ip, self.server_port))
        except Exception as e:
            print("Error happened when connecting to the server.")
            print(e)
        try:
            cs.sendall(bytes(json.dumps(msg.to_dict()), 'utf-8'))
        except Exception as e:
            print("Error happened when sending data to the server.")
            print(e)

    def login(self, username: str, password: str):
        if not username:
            self.error_message = "Please enter username."
        else:
            user = User.User.user(username=username, password=password)
            msg = ConnectingMessage.Message(user, "login", [])
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            try:
                cs.connect((self.server_ip, self.server_port))
            except Exception as e:
                print("Error happened when connecting to the server.")
                print(e)
                self.error_message = "Unknown Error happened"
            try:
                cs.sendall(bytes(json.dumps(msg.to_dict()), 'utf-8'))
                data = cs.recv(self.Buf).decode('utf-8')
                data = json.loads(data)
                print(data)
                data = ConnectingMessage.Message.dict_to_object(data)
                if data.message == "success":
                    self.user = data.user
                else:
                    self.error_message = data.message
            except Exception as e:
                print("Error happened when log in.")
                print(e)
                self.error_message = "Unknown Error happened"
        self.show_error()

    def signup(self, username: str, password: str):
        if not username:
            self.error_message = "Please enter username."
        else:
            user = User.User.user(username=username, password=password)
            msg = ConnectingMessage.Message(user, "signup", [])
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            try:
                cs.connect((self.server_ip, self.server_port))
            except Exception as e:
                print("Error happened when connecting to the server.")
                print(e)
                self.error_message = "Unknown Error happened"
            try:
                cs.sendall(bytes(json.dumps(msg.to_dict()), 'utf-8'))
                data = cs.recv(self.Buf).decode('utf-8')
                data = json.loads(data)
                print(data)
                data = ConnectingMessage.Message.dict_to_object(data)
                if data.message == "success":
                    self.user = data.user
                else:
                    self.error_message = data.message
            except Exception as e:
                print("Error happened when log in.")
                print(e)
                self.error_message = "Unknown Error Happened"
        self.show_error()

    def show_error(self):
        if self.error_message:
            messagebox.showerror("", self.error_message)
            self.error_message = ""

    def receive_message(self):
        while True:
            cs, caddr = self.receiver.accept()
            while True:
                data = cs.recv(self.Buf).decode('utf-8')
                if not data:
                    break
                data = json.loads(data)
                data = ConnectingMessage.Message.dict_to_object(data)
                msg = '[' + time.strftime('%H:%M:%S', time.localtime(float(data.message_time))) + ']' + \
                      data.user.username + ':\n' + data.message
                self.message_queue.put(msg)
            cs.close()


