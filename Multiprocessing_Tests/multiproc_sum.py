import multiprocessing
import requests


def list_sum(l):
    return sum(l)


def request_ec2(ip_address, json_structure):
    return requests.get(url=ip_address, params=json_structure)


if __name__ == '__main__':
    
    lists = [list(range(9000000)), list(range(9000000)), list(range(9000000))]
    pool = Pool()
    result = pool.map(list_sum, lists)

    print(sum(result))
    
