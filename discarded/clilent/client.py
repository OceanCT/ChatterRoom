import socket
import threading



def send_data(data_for_sent:str,Buf:int,server_ip:str,server_port:int):
    addr = (server_ip,server_port)
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    cs.connect(addr)
    data  = cs.recv(Buf).decode('utf-8')
    if not data:
        print("Error happened when connecting to the server.")
    else:
        cs.sendall(bytes(data_for_sent,'utf-8'))
    cs.close()

def send_data_to_server(Buf:int,server_ip:str,server_port:int):
    while True:
        data_for_sent = input("Please input the data you want to send:")
        send_data(data_for_sent,Buf,server_ip,server_port)
    
def get_data_from_server(Buf:int,host_ip:str,host_port:int):
    addr = (host_ip,host_port)
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    ss.bind(addr)
    ss.listen(1)
    while True:
        cs,caddr = ss.accept()
        data = cs.recv(Buf).decode('utf-8')
        print(data)
        cs.close()

if __name__ == '__main__':
    Buf = 102400
    server_ip = '127.0.0.1'
    server_port = 13875
    host_ip = '127.0.0.1'
    host_port = 13985
    threading.Thread(target=send_data_to_server,args=(Buf,server_ip,server_port)).start()
    threading.Thread(target=get_data_from_server,args=(Buf,host_ip,host_port)).start()