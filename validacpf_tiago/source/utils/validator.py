from source.utils.formatter import Formatter


class Validator:

    @classmethod
    def validate(cls, input_string):
        first_digit_weight_dict = dict()
        formatted_string = Formatter.format_it(input_string)

        if len(set(list(formatted_string))) == 1:
            return False

        [first_digit_weight_dict.update({each: index}) for index, each in zip(range(10, 1, -1), formatted_string[:-2])]

        first_digit_mul_list_sum = sum([int(k)*v for k, v in first_digit_weight_dict.items()])
        first_digit_div = divmod(first_digit_mul_list_sum, 11)

        first_digit_remaining = 11 - first_digit_div[1]

        if first_digit_remaining > 9:
            first_digit_remaining = 0

        if first_digit_remaining != int(formatted_string[-2]):
            return False

        second_digit_weight_dict = dict()

        [second_digit_weight_dict.update({each: index}) for index, each in zip(range(11, 1, -1), formatted_string[:-1])]
        second_digit_mul_list_sum = sum([int(k)*v for k, v in second_digit_weight_dict.items()])
        second_digit_div = divmod(second_digit_mul_list_sum, 11)

        second_digit_remaining = 11 - second_digit_div[1]
        
        if second_digit_remaining > 9:
            second_digit_remaining = 0

        if second_digit_remaining != int(formatted_string[-1]):
            return False

        return True
