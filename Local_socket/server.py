import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.211", 2020))
server.listen(5)

while True:
        client, address = server.accept()
        client.send(("authenticating ").encode())
        if ((client.recv()).decode("utf-8") == "python-programming-remote-socket"):
                client.send("welcome to server")
                client.close()
        else:
                client.close()
