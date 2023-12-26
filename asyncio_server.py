from socket import *
from main import fib
import asyncio
from functools import partial

SERVER_ADRESS = ('localhost', 25000)

async def run():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(SERVER_ADRESS)

    server_socket.listen(1)
    print(f"Server listening on {SERVER_ADRESS}")

    loop = asyncio.get_event_loop()

    while True:
        client_socket, client_address = await accept_async(loop, server_socket) # Blocking
        print(f'Connection with {client_address} established')

        connection_task = asyncio.create_task(handle_connection(loop, client_socket=client_socket))
        asyncio.create_task(run_in_background(loop, connection_task))        

async def run_in_background(loop, task):
    await asyncio.sleep(0)  # Yield control to the event loop
    await loop.create_task(task.get_coro())        

async def handle_connection(loop, client_socket):
    while True:
        response = await recv_async(loop, client_socket)
        try:
            response = int(response)
            response = await fib_async(loop, response)
            response = str(response)
        except:
            response = ''
        response = response.encode()       
        await sendall_async(loop, client_socket, response)

async def fib_async(loop, num):
    func = partial(fib, num)    
    return await loop.run_in_executor(None, func)

async def recv_async(loop, client_socket):
    func = partial(client_socket.recv, 1024)
    return await loop.run_in_executor(None, func)

async def sendall_async(loop, client_socket, resp):
    func = partial(client_socket.sendall, resp)
    return await loop.run_in_executor(None, func)

async def accept_async(loop, server_socket):
    return await loop.run_in_executor(None, server_socket.accept)

if __name__ == "__main__":
    asyncio.run(run())