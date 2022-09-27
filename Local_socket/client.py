import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.211", 2020))

print((client.recv(16)).decode("utf-8"))

client.send(bytes("python-programming-remote-socket"), "utf8")

print((client.recv(16)).decode("utf-8"))

client.close()