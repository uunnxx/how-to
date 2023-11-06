import socket


s = socket.socket()

s.connect(('google.com', 80))
s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
print(str(s.recv(4096)))


