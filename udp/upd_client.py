import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port=('127.0.0.1',3030)
while True:
    msg=input("message>>>").encode('utf-8')
    if msg==b'bye':
        break
    sk.sendto(msg,ip_port)
    info,addr=sk.recvfrom(1024)

    print(info)
sk.close()