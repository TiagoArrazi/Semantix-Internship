import socket
from concurrent.futures import ProcessPoolExecutor
from time import time
from numpy import linspace
import select


addrs = dict(addr_1={"ip": "192.168.43.227",
                     "port": 13001},
             addr_2={"ip": "192.168.43.189",
                     "port": 13000}
             )

local_addr = dict(ip="192.168.43.118",
                  port=14000)


def send_params(range_, sock):
    header_length = len(range_)
    data = range_.encode("utf-8")
    print('Sending range<{}> to socket {}'.format(data, sock))
    sock.send(data)


def mk_ranges(interval_list, amount):
    return [range(interval_list[i], interval_list[i + 1]) for i in range(amount)]


def receive_data(client_socket):
    data = client_socket.recv(50)

    return {"data": data}


def gather(client_sock_1, t):
    client_sock_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_sock_1.bind((local_addr["ip"], local_addr["port"]))
    print('Listening on {}:{}'.format(local_addr["ip"], local_addr["port"]))
    client_sock_1.listen()

    acc = 0

    sockets_list = [client_sock_1]

    while True:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

        for notified_socket in read_sockets:
            if notified_socket == client_sock_1:
                sockets_list.append(notified_socket)
                client_socket, client_address = client_sock_1.accept()
                data = receive_data(client_socket)

                if data is False:
                    continue

                acc += int(data["data"])
                print("RESULT = {}".format(acc))
                print("TIME = {}".format(time() - t))


if __name__ == '__main__':
    start = time()

    intervals = [int(each) for each in list(linspace(0, 1800000000, 3))]
    range_list = mk_ranges(interval_list=intervals, amount=2)
    processed_range_list = ["{} {}".format(r[0], r[-1]) for r in range_list]

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((addrs["addr_1"]["ip"], addrs["addr_1"]["port"]))
    client_sock.setblocking(False)

    send_params(processed_range_list[0], client_sock)

    client_sock.close()

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_sock.connect((addrs["addr_2"]["ip"], addrs["addr_2"]["port"]))
    client_sock.setblocking(False)

    send_params(processed_range_list[1], client_sock)
    client_sock.close()

    gather(socket.socket(socket.AF_INET, socket.SOCK_STREAM), start)
