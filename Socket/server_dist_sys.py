import socket
from numpy import linspace
from concurrent.futures import ProcessPoolExecutor
import select


def sum_list(l):
    acc = 0
    for each in l:
        acc += each

    return acc


addr = dict(ip="127.0.0.1",
            port=13000)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((addr["ip"], addr["port"]))
server_socket.listen()

sockets_list = [server_socket]
clients = {}


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
