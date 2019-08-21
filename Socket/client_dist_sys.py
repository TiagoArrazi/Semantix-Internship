import socket
from concurrent.futures import ProcessPoolExecutor
from time import time
from numpy import linspace

addrs = dict(addr_1={"ip": "127.0.0.1",
                     "port": 13000},
             addr_2={"ip": "127.0.0.1",
                     "port": 13001}
             )


def send_params(ranges, sock):
    sock.send(ranges.encode("utf-8"))


def mk_ranges(interval_list, amount):
    return [range(interval_list[i], interval_list[i + 1]) for i in range(amount)]


if __name__ == '__main__':
    start = time()

    intervals = [int(each) for each in list(linspace(0, 1800000000, 3))]
    range_list = mk_ranges(interval_list=intervals, amount=2)
    processed_range_list = ["{} {}".format(r[0], r[-1]) for r in range_list]

    client_sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_sock_1.connect((addrs["addr_1"]["ip"], addrs["addr_1"]["port"]))
    client_sock_2.connect((addrs["addr_2"]["ip"], addrs["addr_2"]["port"]))

    sock_list = [client_sock_1, client_sock_2]

    with ProcessPoolExecutor as executor:
        futures = list()
        for r in executor.map(send_params, (processed_range_list, sock_list)):
            futures.append(r)

        print("RESULT: {}".format(sum(futures)))
        print("TIME: {}".format(time() - start))

