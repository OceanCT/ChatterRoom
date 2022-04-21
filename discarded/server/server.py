import socket
import time
import threading
def cs_listen(cs,caddr):
    print("Connection coming from :",caddr)
    data =  "Welcome.\n"
    cs.sendall(bytes(data,'utf-8'))
    while True:
        data = cs.recv(Buf).decode('utf-8')
        if not data:
            break
        data = '[%s][%s]%s\n'%(time.ctime(),caddr,data)
        print(data)
    cs.close()

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 13875
    Buf = 1024
    addr = (host,port)
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    ss.bind(addr)
    ss.listen(20)
    while True:
        cs,caddr = ss.accept()
        threading.Thread(target=cs_listen,args=(cs,caddr)).start()
    ss.close()
