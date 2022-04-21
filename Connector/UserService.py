import pymysql
from Connector import User


class UserService:

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
        sql = 'create table if not exists user(username varchar(255),password varchar(255)) '
        self.cursor.execute(sql)
        self.conn.commit()

    def find_user_by_username(self, username: str):
        sql = "select * from user where username = '%s';" % username
        self.cursor.execute(sql)
        lis = self.cursor.fetchall()
        self.conn.commit()
        if len(lis):
            return User.User.user(lis[0][0], lis[0][1])
        else:
            return User.User.user()

    def insert_user(self, user: User.User):
        sql = "insert into user values('%s','%s');" % (user.username, user.password)
        self.cursor.execute(sql)
        self.conn.commit()
