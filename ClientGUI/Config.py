import yaml


class LoginFrameConfig:
    def __init__(self, root_height, root_width, label_width, username_x, username_y, password_x, password_y,
                 username_label_x, username_label_y, password_label_x, password_label_y, login_button_x, login_button_y,
                 signup_button_x, signup_button_y):
        self.root_height = root_height
        self.root_width = root_width
        self.label_width = label_width
        self.username_x = username_x
        self.username_y = username_y
        self.password_x = password_x
        self.password_y = password_y
        self.username_label_x = username_label_x
        self.username_label_y = username_label_y
        self.password_label_x = password_label_x
        self.password_label_y = password_label_y
        self.login_button_x = login_button_x
        self.login_button_y = login_button_y
        self.signup_button_x = signup_button_x
        self.signup_button_y = signup_button_y

    @classmethod
    def convert_dict_to_object(cls, dict_data):
        return cls(
            dict_data['root_height'],
            dict_data['root_width'],
            dict_data['label_width'],
            dict_data['username_x'],
            dict_data['username_y'],
            dict_data['password_x'],
            dict_data['password_y'],
            dict_data['username_label_x'],
            dict_data['username_label_y'],
            dict_data['password_label_x'],
            dict_data['password_label_y'],
            dict_data['login_button_x'],
            dict_data['login_button_y'],
            dict_data['signup_button_x'],
            dict_data['signup_button_y']
        )


class ChatFrameConfig():
    def __init__(
            self, root_height, root_width,
            msg_box_height, msg_box_width, msg_box_x, msg_box_y,
            input_box_height, input_box_width, input_box_x, input_box_y,
            chatter_box_height, chatter_box_width, chatter_box_x, chatter_box_y,
            send_button_height, send_button_width, send_button_x, send_button_y
    ):
        self.root_height = root_height
        self.root_width = root_width
        self.msg_box_height = msg_box_height
        self.msg_box_width = msg_box_width
        self.msg_box_x = msg_box_x
        self.msg_box_y = msg_box_y
        self.input_box_height = input_box_height
        self.input_box_width = input_box_width
        self.input_box_x = input_box_x
        self.input_box_y = input_box_y
        self.chatter_box_height = chatter_box_height
        self.chatter_box_width = chatter_box_width
        self.chatter_box_x = chatter_box_x
        self.chatter_box_y = chatter_box_y
        self.send_button_x = send_button_x
        self.send_button_y = send_button_y
        self.send_button_width = send_button_width
        self.send_button_height = send_button_height

    @classmethod
    def convert_dict_to_object(cls, dict_data):
        return cls(
            dict_data['root_height'],
            dict_data['root_width'],
            dict_data['msg_box_height'],
            dict_data['msg_box_width'],
            dict_data['msg_box_x'],
            dict_data['msg_box_y'],
            dict_data['input_box_height'],
            dict_data['input_box_width'],
            dict_data['input_box_x'],
            dict_data['input_box_y'],
            dict_data['chatter_box_height'],
            dict_data['chatter_box_width'],
            dict_data['chatter_box_x'],
            dict_data['chatter_box_y'],
            dict_data['send_button_height'],
            dict_data['send_button_width'],
            dict_data['send_button_x'],
            dict_data['send_button_y'],
        )


class Config:
    def __init__(self):
        yaml_path = r'./config.yaml'
        with open(yaml_path, mode='rb') as f:
            infos = yaml.load(f, Loader=yaml.FullLoader)
        self.loginFrameConfig = LoginFrameConfig.convert_dict_to_object(infos['loginFrameConfig'])
        self.chatFrameConfig = ChatFrameConfig.convert_dict_to_object(infos['chatFrameConfig'])
