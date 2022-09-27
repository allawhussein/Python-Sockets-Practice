import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.211", 2020))
server.listen(5)

while True:
        client, address = server.accept()
        client.send(('HTTP/1.0 200 OK\n\n').encode())
        client.send(('<html><head><title>Welcome %!</title></head>').encode()) 
        client.send(('<body><h1>Follow the link...</h1>').encode()) 
        client.send(('All the server needs to do is ').encode()) 
        client.send(('to deliver the text to the socket. ').encode())
        client.send(('It delivers the HTML code for a link, ').encode())
        client.send(('and the web browser converts it. <br><br><br><br>').encode())
        client.send(('<font size="7"><center> <a href="http://python.about.com/index.html">Click me!</a> </center></font>').encode()) 
        client.send(('<br><br>The wording of your request was:').encode()) 
        client.send(('</body></html>').encode())