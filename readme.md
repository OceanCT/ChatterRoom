# 项目结构

```

.
├── ClientGUI
│   ├── __init__.py
│   ├── ChatFrame.py
│   ├── Config.py
│   ├── config.yaml
│   └── LoginFrame
├── Connector
│   ├── __init__.py
│   ├── Client.py
│   ├── ConnectingMessage.py
│   ├── Server.py
│   ├── User.py
│   ├── UserService.py
│──── client.py
│──── config.yaml
│──── server.py
│──── readme.md


```

# 使用需知

## Server

server.py运行在服务端，无需调试

## Client

client.py运行在客户端，这里需要将Connector下的Client里的server_ip调整为服务端ip,


## 关于一台PC上多个账号的问题

运行client.py时需要调整40行初始化listener_port为一个空闲的端口号，不能与之前运行的端口号重复，
默认情况下，这个端口号是13876