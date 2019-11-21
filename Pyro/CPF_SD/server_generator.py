import Pyro4
import time


class DigitGenerator:    

    @classmethod
    def generate_verification_digits(cls, input_string):

        digits = list(int(d) for d in list(input_string))

        if len(digits) == 9:

            d1_dict = dict()

            [d1_dict.update({index: digit})
             for index, digit in zip(range(10, 1, -1), digits)]

            d1_weight_quot, d1_weight_rem = divmod(sum([k * v
                                                        for k, v in d1_dict.items()]), 11)
            d1 = 0 if d1_weight_rem < 2 else 11 - d1_weight_rem

            digits.append(d1)

            d2_dict = dict()

            [d2_dict.update({index: digit})
             for index, digit in zip(range(11, 1, -1), digits)]

            d2_weight_quot, d2_weight_rem = divmod(sum([k * v
                                                        for k, v in d2_dict.items()]), 11)
            d2 = 0 if d2_weight_rem < 2 else 11 - d2_weight_rem

            digits.append(d2)

            digits = [str(d) for d in digits]

            return ''.join(digits)

        elif len(digits) == 12:

            weigths_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

            d1_weight_quot, d1_weight_rem = divmod(sum([k * v
                                                        for k, v in zip(digits, weigths_1)]), 11)

            d1 = 0 if d1_weight_rem < 2 else 11 - d1_weight_rem

            digits.append(d1)

            weigths_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

            d2_weight_quot, d2_weight_rem = divmod(sum([k * v
                                                        for k, v in zip(digits, weigths_2)]), 11)

            d2 = 0 if d2_weight_rem < 2 else 11 - d2_weight_rem

            digits.append(d2)

            digits = [str(d) for d in digits]

            return ''.join(digits)

        return False


if __name__ == '__main__':
     
    verifier = Pyro4.Proxy('PYRONAME:verifier')

    with open('BASEPROJETO.txt', 'r') as f:
        raw = [each.replace('\n', '').strip() for each in f.readlines()]

        start_total = time.time()

        for each in raw:
            start = time.time()
            print('{} - {}'.format(verifier.validate(DigitGenerator.generate_verification_digits(each)),
                                   time.time() - start))

        print('Total time: {}'.format(time.time() - start_total))
        print('Sequences validated: {}'.format(len(raw)))
