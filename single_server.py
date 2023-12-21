from socket import *
from main import fib

SERVER_ADRESS = ('localhost', 25000)

def run():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(SERVER_ADRESS)

    server_socket.listen(1)
    print(f"Server listening on {SERVER_ADRESS}")

    while True:
        client_socket, client_address = server_socket.accept() # Blocking        
        while True:
            response = str(fib(int(client_socket.recv(1024))))        
            client_socket.sendall(response.encode())

if __name__ == "__main__":
    run()