import tkinter
from ClientGUI import Config


class ChatFrame:
    def __init__(self):
        self.message = ""
        config = Config.Config().chatFrameConfig
        self.root = tkinter.Tk()
        self.root.title("Chatting")
        self.root.geometry("%sx%s" % (config.root_width, config.root_height))
        self.msg_box = tkinter.Text(self.root, bd=5, font='Consolas')
        self.msg_box.place(x=config.msg_box_x, y=config.msg_box_y, height=config.msg_box_height,
                           width=config.msg_box_width)
        self.input_box = tkinter.Text(self.root, bd=5, font='Consolas')
        self.input_box.place(x=config.input_box_x, y=config.input_box_y, height=config.input_box_height,
                             width=config.input_box_width)
        self.send_button = tkinter.Button(self.root, text="Send", command=self.quit_root)
        self.send_button.place(x=config.send_button_x, y=config.send_button_y, height=config.send_button_height,
                               width=config.send_button_width)
        self.chatter_box = tkinter.Text(self.root, bd=5, font='Consolas')
        self.chatter_box.place(x=config.chatter_box_x, y=config.chatter_box_y, height=config.chatter_box_height,
                               width=config.chatter_box_width)

    def quit_root(self):
        self.root.quit()

    def show(self):
        self.root.mainloop()

    def get_input(self):
        self.message = self.input_box.get("1.0", tkinter.END)
        self.input_box.delete('1.0', tkinter.END)
        return self.message

