import Pyro4


@Pyro4.expose
class Verifier: 

    @classmethod
    def validate(cls, input_string):

        digits = list(int(d) for d in list(input_string))

        if len(digits) == 11:

            d1 = digits[-2]
            d2 = digits[-1]

            d1_dict = dict()

            [d1_dict.update({index: digit})
             for index, digit in zip(range(10, 1, -1), digits[:-2])]

            d1_weight_quot, d1_weight_rem = divmod(sum([k * v for k, v in d1_dict.items()]) * 10, 11)

            d2_dict = dict()

            [d2_dict.update({index: digit})
             for index, digit in zip(range(11, 1, -1), digits[:-1])]

            d2_weight_quot, d2_weight_rem = divmod(sum([k * v for k, v in d2_dict.items()]) * 10, 11)

            d1_weight_rem = d1_weight_rem if d1_weight_rem < 10 else 0
            d2_weight_rem = d2_weight_rem if d2_weight_rem < 10 else 0

            return False if d1_weight_rem is not d1 or d2_weight_rem is not d2 else True

        elif len(digits) == 14:

            d1 = digits[-2]
            d2 = digits[-1]

            weigths_1 = [6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]

            d1_weight_quot, d1_weight_rem = divmod(sum([k * v
                                                        for k, v in zip(digits, weigths_1)]), 11)

            weigths_2 = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]

            d2_weight_quot, d2_weight_rem = divmod(sum([k * v
                                                        for k, v in zip(digits, weigths_2)]), 11)

            d1_weight_rem = d1_weight_rem if d1_weight_rem < 10 else 0
            d2_weight_rem = d2_weight_rem if d2_weight_rem < 10 else 0

            return False if d1_weight_rem is not d1 or d2_weight_rem is not d2 else True

        return False


if __name__ == '__main__':
    
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(Verifier)
    ns.register('verifier', uri)
    print('Started')

    daemon.requestLoop()

