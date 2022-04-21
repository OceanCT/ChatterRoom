import pymysql
from Connector import ConnectingMessage
from Connector import User


class ConnectingMessageService:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='SocketChat',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()
        sql = 'create table if not exists message(' \
              'username varchar(255),message varchar(255),message_time varchar(255)) '
        self.cursor.execute(sql)
        self.conn.commit()

    def fetch_message(self):
        sql = "select * from message"
        if self.cursor.execute(sql) > 20:
            lis = self.cursor.fetchmany(20)
        else:
            lis = self.cursor.fetchall()
        self.conn.commit()
        res = []
        for k in lis:
            msg = ConnectingMessage.Message(User.User.user(k[0]),k[1])
            msg.message_time = k[2]
            res.append(msg)
        return res

    def insert_message(self, message: ConnectingMessage):
        sql = "insert into message values('%s','%s','%s')" % (
            message.user.username, message.message, message.message_time)
        self.cursor.execute(sql)
        self.conn.commit()
