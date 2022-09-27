import socket
import random

address = "127.0.0.1"
port = 1010

def PRG(key):
        #what ever the key should do
        return 1+1

def OTPciper (text, key):
      print ("cipher")  

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


if __name__ == "__main__" :
        while (True):
                try:
                        connected = 1
                        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        server.bind((address, port))
                except:
                        port += 1 
                        connected = 0

                if (connected == 1):
                        print ("binded at", address, " - ", port)
                        break

        server.listen(1)

        while True:
                client, client_address = server.accept()
                key_seed = handshake(client)
                crypto_key = PRG(key_seed)