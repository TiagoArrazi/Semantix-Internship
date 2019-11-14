
class CPFHandler:

    @staticmethod
    def generate_verification_digits(cpf):
        digits = list(int(d) for d in list(cpf))

        d1_dict = dict()
        [d1_dict.update({index: digit}) for index, digit in zip(range(10, 1, -1), digits)]
        d1_weight_quot, d1_weight_rem = divmod(sum([k * v for k, v in d1_dict.items()]), 11)

        d1 = 0 if d1_weight_rem < 2 else 11 - d1_weight_rem

        digits.append(d1)

        d2_dict = dict()
        [d2_dict.update({index: digit}) for index, digit in zip(range(11, 1, -1), digits)]
        d2_weight_quot, d2_weight_rem = divmod(sum([k * v for k, v in d2_dict.items()]), 11)

        d2 = 0 if d2_weight_rem < 2 else 11 - d2_weight_rem

        return '{}{}'.format(d1, d2)

    @staticmethod
    def validate_cpf(cpf):

        digits = list(int(d) for d in list(cpf))

        d1 = digits[-2]
        d2 = digits[-1]

        d1_dict = dict()

        [d1_dict.update({index: digit}) for index, digit in zip(range(10, 1, -1), digits[:-2])]
        d1_weight_quot, d1_weight_rem = divmod(sum([k * v for k, v in d1_dict.items()]) * 10, 11)

        d2_dict = dict()

        [d2_dict.update({index: digit}) for index, digit in zip(range(11, 1, -1), digits[:-1])]
        d2_weight_quot, d2_weight_rem = divmod(sum([k * v for k, v in d2_dict.items()]) * 10, 11)

        return False if d1_weight_rem is not d1 or d2_weight_rem is not d2 else True


if __name__ == '__main__':
    with open('CPF.txt') as f:
        cpf_list = ' '.join(list('{}{}'.format(each.replace('\n', ''),
                                               CPFHandler.generate_verification_digits(each.replace('\n', '')))
                            for each in f.readlines()))

        [print(CPFHandler.validate_cpf(cpf)) for cpf in cpf_list.split(' ')]
