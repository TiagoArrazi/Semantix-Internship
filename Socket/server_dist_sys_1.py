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


def mk_range(range_bytes):
    str_ranges = range_bytes.decode("utf-8")
    ranges = str_ranges.split(" ")

    return range(int(ranges[0]), int(ranges[1]))


def receive_data(client_socket):

    data_header = client_socket.recv(HEADER_LENGTH)

    if not len(data_header):
        return False

    data_length = len(data_header.decode('utf-8').strip())
    return {"data": data_header, "data_sender": client_socket.recv(data_length)}



addr = dict(ip="127.0.0.1",
            port=13000)


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

            sockets_list.append(client_socket)
            clients[client_socket] = data

            print("Data range<{}> received from {}:{}, username: {}".format(data["data"].decode("utf-8"), 
                                                                            *client_address,
                                                                            data["data_sender"].decode("utf-8")))        
            
