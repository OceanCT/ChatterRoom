# 使用需知

## Server

server.py运行在服务端，无需调试

## Client

client.py运行在客户端，这里需要将Connector下的Client里的server_ip调整为服务端ip

## 关于多台设备通信

在不修改源码的基础上这里支持多台设备连接，但是每台PC仅能有一个账号在用，并且需要保持13876端口号的正常通信