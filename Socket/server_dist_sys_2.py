import socket
from numpy import linspace
from concurrent.futures import ProcessPoolExecutor
import select


HEADER_LENGTH = 10

def sum_list(l):
    acc = 0
    for each in l:
        acc += each

    return acc


def receive_data(client_socket):
    try:

        data_header = client_socket.recv(HEADER_LENGTH)

        if not len(data_header):
            return False

        data_length = int(data_header.decode('utf-8').strip(0))
        return {"header": data_header, "data": client_socket.recv(data_length)}

    except:
        return False


addr = dict(ip="127.0.0.1",
            port=13001)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((addr["ip"], addr["port"]))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

print(f"Listening for connections on {addr['ip']}:{addr['port']}...")

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            data = receive_data(client_socket)

            if data is False:
                continue

            socket_list.append(client_socket)
            clients[client_socket] = data

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address,
                                                                            data["data"].decode("utf-8")))

