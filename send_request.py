from socket import *

def create_connection(server_address):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(server_address)
    return client_socket

def send_request(socket, request):
    socket.sendall(str(request).encode())
    response = socket.recv(1024)


    

