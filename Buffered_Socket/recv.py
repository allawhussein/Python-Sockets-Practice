import BS_library
import socket

location = "D:\\programming\\python\\Sockets"
destination = (("127.0.0.1", 1111))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(destination)

BS_library.recv_file(location, client)