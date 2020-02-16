import socket
import subprocess

sk = socket.socket(type=socket.SOCK_DGRAM)
addr=('127.0.0.1',3000)
sk.sendto(b'hello',addr)
while True:
    cmd,addr = sk.recvfrom(1024)
    ret = subprocess.Popen(cmd.decode('gbk'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = ret.stdout.read().decode('gbk')
    std_err = ret.stderr.read().decode("gbk")
    print(std_out)
    print(std_err)
    sk.sendto(std_out.encode('utf-8'),addr)
    sk.sendto(std_err.encode('utf-8'),addr)
sk.close()