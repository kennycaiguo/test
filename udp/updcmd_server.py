import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',3000))

msg,addr = sk.recvfrom(1024)

while True:
    cmd = input('Enter Command>>>')
    if cmd=='q':
        break
    sk.sendto(cmd.encode('utf-8'),addr)
    msg,addr=sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()