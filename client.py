import threading
import tkinter
from Connector import *
from ClientGUI import *
import queue


def loginAndSignUp():
    login_frame = LoginFrame.LoginFrame()
    login_frame.login_button.configure(command=lambda: [
        client.login(login_frame.get_username(), login_frame.get_password()),
        login_frame.is_quit(client.user.username)
    ])
    login_frame.signup_button.configure(command=lambda: [
        client.signup(login_frame.get_username(), login_frame.get_password()),
        login_frame.is_quit(client.user.username)
    ])
    login_frame.show()
    login_frame.root.destroy()
    msg_queue.put(1)


def show_message(chat_frame:ChatFrame.ChatFrame):
    while True:
        chat_frame.msg_box.insert(tkinter.END, client.message_queue.get())


def Chat():
    msg_queue.get()
    chat_frame = ChatFrame.ChatFrame()
    chat_frame.send_button.configure(command=lambda: [
        client.send_message(chat_frame.get_input(), [])
    ])
    threading.Thread(target=show_message,args=(chat_frame,)).start()
    chat_frame.show()


if __name__ == '__main__':
    msg_queue = queue.Queue()
    client = Client.Client()
    threading.Thread(target=loginAndSignUp).start()
    threading.Thread(target=Chat).start()
