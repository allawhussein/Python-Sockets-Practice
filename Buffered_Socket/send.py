import BS_library
import socket

location = "D:\\programming\\python\\Sockets\\javanotes.pdf"
destination = (("127.0.0.1", 1111))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(destination)
server.listen(1)
client, address = server.accept()

BS_library.send_file(location, client)