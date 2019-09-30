import socket
from numpy import linspace
from concurrent.futures import ProcessPoolExecutor
import select
from pprint import pprint


HEADER_LENGTH = 50


def sum_list(l):
    acc = 0
    for each in l:
        acc += each
        if each % 10000000 == 0:
            print(f"ACC: {acc:,}")

    return acc


def ranges_from_intervals(l, amount):
    return [range(l[i], l[i + 1]) for i in range(amount)]


def mk_range(range_bytes):
    str_ranges = range_bytes.decode("utf-8")
    ranges = str_ranges.split(" ")

    return range(int(ranges[0]), int(ranges[1]) + 1)


def receive_data(client_socket):

    data = client_socket.recv(HEADER_LENGTH)

    if not len(data):
        return False

    return {"data": data}


addr = dict(ip="192.168.0.46",
            port=13000)


client_addr = dict(ip="192.168.0.14",
                   port=20000)

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

            print("Data range<{}> received from {}:{}".format(data["data"].decode("utf-8"), *client_address))

    ranges = mk_range(data["data"])
    # intervals = [int(each) for each in list(linspace(ranges[0], ranges[-1], 4))]
    # range_list = ranges_from_intervals(intervals, 3)
    break



print(f"EXECUTING SUM IN RANGE LIST: {ranges}")
s = sum_list(ranges)
print(f"{s:,}")
final_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to {}:{}".format(client_addr["ip"], client_addr["port"]))
final_sock.connect((client_addr["ip"], client_addr["port"]))
print("Connected!")
print("Sending data {}".format(s))
final_sock.send(str(s).encode("utf-8"))
final_sock.close()
