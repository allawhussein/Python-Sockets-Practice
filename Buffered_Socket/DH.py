from sys import argv
import socket
import random

def handshake(target):
        prime_1 = 11364357231821165769892549063506171923
        prime_2 = 143166232059652401956226505575319723543

        private_number = random.getrandbits(128)

        public_number = pow(prime_1, private_number, prime_2)

        public_number_string = str(public_number)
        target.send(bytes(public_number_string, "utf-8"))

        recieved_number = target.recv(128)
        recieved_number = int (recieved_number.decode())

        random_key = pow(recieved_number, private_number, prime_2)

        return random_key

if __name__ == "main":

        if argv[1] == "server":
                print ("actin as server")
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                connected = 0
                ip_address = argv[2]
                port = argv[3]

                while connected == 0:
                        try:
                                server.bind(ip_address, port)
                                connected = 1
                        except:
                                print("unable to bind")
                                connected = 0

                                ip_address = input("re-enter the IP address (enter space to reuse old one)")
                                if ip_address == ' ':
                                        ip_address = argv[2]
                                
                                port = int (input("re-enter the port number (digits only)"))

                server.listen(1)
                client, client_address = server.accept()
                key_seed = handshake(client)
                print(key_seed)

        elif argv[1] == "client":
                print("acting as client")
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                ip_address = argv[2]
                port = argv[3]

                connedted = 0

                while connected == 0:
                        try:
                                client.connect((ip_address, port))
                                connected = 1

                        except:
                                ip_address = input("re-enter IP address")
                                port = int (input ("re-enter the port number"))
                                connected = 0

        else:
                print("your first argument is wrong")