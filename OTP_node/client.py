import socket
import random

address = "127.0.0.1"
port = 1010

def handshake(target):
        prime_1 = 11364357231821165769892549063506171923
        prime_2 = 143166232059652401956226505575319723543

        private_number = random.getrandbits(128)

        public_number = pow(prime_1, private_number, prime_2)

        recieved_number = target.recv(2084)
        recieved_number = int(recieved_number.decode())

        public_number_string = str(public_number)
        target.send(bytes(public_number_string, "utf-8"))

        random_key = pow(recieved_number, private_number, prime_2)

        return random_key

if __name__ == "__main__" :
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((address, port))
        print(handshake(client))