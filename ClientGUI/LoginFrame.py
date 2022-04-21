import tkinter
from ClientGUI import Config


class LoginFrame:
    def __init__(self):
        self.username = None
        self.password = None
        config = Config.Config().loginFrameConfig
        self.root = tkinter.Tk()
        self.root.title("Login")
        self.root.geometry("%sx%s" % (config.root_width, config.root_height))
        self.username_label = tkinter.Label(self.root, text="Username:")
        self.username_label.place(x=config.username_label_x, y=config.username_label_y)
        self.username_entry = tkinter.Entry(self.root, width=config.label_width)
        self.username_entry.place(x=config.username_x, y=config.username_y)
        self.password_label = tkinter.Label(self.root, text="Password:")
        self.password_label.place(x=config.password_label_x, y=config.password_label_y)
        self.password_entry = tkinter.Entry(self.root, width=config.label_width)
        self.password_entry.place(x=config.password_x, y=config.password_y)
        self.login_button = tkinter.Button(self.root, text="Login", command=self.quit_root)
        self.login_button.place(x=config.login_button_x, y=config.login_button_y)
        self.signup_button = tkinter.Button(self.root, text="SignUp", command=self.quit_root)
        self.signup_button.place(x=config.signup_button_x, y=config.signup_button_y)

    def quit_root(self):
        self.root.quit()

    def get_username(self):
        self.username = self.username_entry.get()
        return self.username

    def get_password(self):
        self.password = self.password_entry.get()
        return self.password

    def show(self):
        self.root.mainloop()

    def is_quit(self,username=""):
        if username:
            self.root.quit()
