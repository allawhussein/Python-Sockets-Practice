import socket

def send_file(location, target):
        file = open(location, "rb")

        packet = file.read(64)
        while (len(packet) != 0):
                packet = file.read(64)

                target.send(packet)

        target.close()
        file.close()

def recv_file(location,target):
        filename = input("recv the file as")
        file = open(location + filename, "wb")

        while True:
                data = target.recv(64)

                if (len(data) < 64):
                        break
                
                file.write(data)

                
        file.close()
        target.close()
if __name__ == "__main__":
        ip_address = input("enter the IP address")
        port = int (input ("enter the port numbre"))

        target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        choice = input ("the node is: ")
        if (choice == "reciever"):
                target.bind((ip_address, port))
                target.listen(1)
                client, address = target.accept()

                location = input("enter the location: ")

                send_file(location, client)
        
        elif (choice == "client"):
                target.connect((ip_address, port))
                recv_file(location, target)