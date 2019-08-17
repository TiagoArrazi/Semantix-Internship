from sys import argv

symbols = {"1": "I",
           "5": "V",
           "10": "X",
           "50": "L",
           "100": "C",
           "500": "D",
           "1000": "M"}


def make_it_roman(number):
    if 900 <= int(number) <= 1300:
        if number == "1000":
            return symbols[number]

        amount = (1000 - int(number)) // 100
        if amount < 0:
            return f"{symbols['100']}{symbols['1000']}"
        if amount > 0:
            return f"{symbols['1000']}{amount * symbols['100']}"

    if 400 <= int(number) <= 800:
        if number == "500":
            return symbols[number]

        amount = (500 - int(number)) // 10
        if amount < 0:
            return f"{symbols['100']}{symbols['500']}"
        if amount > 0:
            return f"{symbols['500']}{amount * symbols['100']}"

    if 90 <= int(number) <= 300:
        if number == "100":
            return symbols[number]

        amount = (100 - int(number)) // 10
        if amount < 0:
            return f"{symbols['10']}{symbols['100']}"
        if amount > 0:
            return f"{symbols['100']}{amount * symbols['10']}"

    if 60 <= int(number) <= 80:
        if number == "50":
            return symbols[number]

        amount = (50 - int(number)) // 10
        if amount < 0:
            return f"{symbols['10']}{symbols['50']}"
        if amount > 0:
            return f"{symbols['50']}{amount * symbols['10']}"

    if 9 <= int(number) <= 30:
        if number == "10":
            return symbols[number]

        amount = 10 - int(number)
        if amount < 0:
            return f"{symbols['1']}{symbols['10']}"
        if amount > 0:
            return f"{symbols['10']}{amount * symbols['1']}"

    if 4 <= int(number) <= 8:
        if number == "5":
            return symbols[number]

        amount = 10 - int(number)
        if amount < 0:
            return f"{symbols['1']}{symbols['5']}"
        if amount > 0:
            return f"{symbols['5']}{amount * symbols['1']}"

    else:
        return int(number) * symbols["1"]


def convert_digits(number):
    strip_number_list = [(10 ** index) // 10 * int(n)
                         for index, n
                         in zip(range(len(number), 0, -1), number)]

    converted_number_list = list()

    for item in strip_number_list:
        converted_number_list.append(make_it_roman(str(item)))

    return ''.join(converted_number_list)


if __name__ == "__main__":

    if 0 < int(argv[1]) <= 3000:
        print(convert_digits(argv[1]))

    else:
        print("Invalid input!")
