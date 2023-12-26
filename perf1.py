from single_server import SERVER_ADRESS
from send_request import send_request, create_connection

import time

def hammer_server():
    start = time.time()
    request_count = 0
    socket = create_connection(SERVER_ADRESS)

    while True:
        send_request(socket=socket, request=20)
        request_count+=1
        if time.time() - start > 1:
            print(request_count)
            request_count = 0
            start = time.time()       

hammer_server()