import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 65432))
sock.send(b'c')

data = sock.recv(1024)
sock.close()

print(data)