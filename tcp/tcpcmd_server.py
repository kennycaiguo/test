import socket

sk = socket.socket()
sk.bind(('127.0.0.1',3000))
sk.listen()
conn,addr = sk.accept()

while True:
    cmd = input("enter command>>>")
    conn.send(cmd.encode('utf-8'))
    ret = conn.recv(1024).decode('utf-8')

    print(ret)
conn.close()
sk.close()

