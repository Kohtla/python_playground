from socket import socket, AF_INET, SOCK_STREAM
from main import fib
import threading

SERVER_ADRESS = ("localhost", 25000)


def run():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(SERVER_ADRESS)

    server_socket.listen(1)
    print(f"Server listening on {SERVER_ADRESS}")

    while True:
        client_socket, client_address = server_socket.accept()  # Blocking
        print(f"Connection with {client_address} established")

        thread = threading.Thread(target=handle_connection, args=(client_socket,))
        thread.start()


def handle_connection(client_socket):
    while True:
        response = client_socket.recv(1024)
        try:
            response = int(response)
            response = fib(response)
            response = str(response)
        except Exception:
            response = ""
        response = response.encode()
        client_socket.sendall(response)


if __name__ == "__main__":
    run()
