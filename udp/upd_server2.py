import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',3030))
while True:
    ret,addr=sk.recvfrom(1024)
    if ret==b'bye':
        break
    print(ret)
    msg=input("your reply:>>>")
    sk.sendto(msg.encode("utf-8"),addr)
sk.close()