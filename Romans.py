from random import randint

symbols = {"1": "I",
           "5": "V",
           "10": "X",
           "50": "L",
           "100": "C",
           "500": "D",
           "1000": "M"}


def make_it_roman(number):
    if 900 <= int(number) <= 3000:
        mult = divmod(int(number), 1000)

        if mult[0] > 0 and mult[1] == 0:
            return symbols["1000"] * mult[0]

        c_amount = (1000 - int(number)) // 100

        if c_amount > 0:
            return f"{symbols['100']}{symbols['1000']}"
        if c_amount < 0:
            return f"{symbols['1000']}{abs(c_amount) * symbols['100']}"

    elif 400 <= int(number) <= 800:
        if number == "500":
            return symbols["500"]

        c_amount = (500 - int(number)) // 100

        if c_amount > 0:
            return f"{symbols['100']}{symbols['500']}"
        if c_amount < 0:
            return f"{symbols['500']}{abs(c_amount) * symbols['100']}"

    elif 90 <= int(number) <= 300:
        mult = divmod(int(number), 100)

        if mult[0] > 0 and mult[1] == 0:
            return symbols["100"] * mult[0]

        c_amount = (100 - int(number)) // 10

        if c_amount > 0:
            return f"{symbols['10']}{symbols['100']}"
        if c_amount < 0:
            return f"{symbols['100']}{abs(c_amount) * symbols['10']}"

    elif 40 <= int(number) <= 80:
        if number == "50":
            return symbols["50"]

        c_amount = (50 - int(number)) // 10

        if c_amount > 0:
            return f"{symbols['10']}{symbols['50']}"
        if c_amount < 0:
            return f"{symbols['50']}{abs(c_amount) * symbols['10']}"

    elif 9 <= int(number) <= 30:
        mult = divmod(int(number), 10)

        if mult[0] > 0 and mult[1] == 0:
            return symbols["10"] * mult[0]

        c_amount = (10 - int(number))

        if c_amount > 0:
            return f"{symbols['1']}{symbols['10']}"
        if c_amount < 0:
            return f"{symbols['10']}{abs(c_amount) * symbols['1']}"

    elif 4 <= int(number) <= 8:
        if number == "5":
            return symbols["5"]

        c_amount = (5 - int(number))

        if c_amount > 0:
            return f"{symbols['1']}{symbols['5']}"
        if c_amount < 0:
            return f"{symbols['5']}{abs(c_amount) * symbols['1']}"

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
    arabic_list = [str(randint(1, 3000)) for i in range(20)]
    [print("{} -> {}".format(arabic, convert_digits(arabic))) for arabic in arabic_list]
