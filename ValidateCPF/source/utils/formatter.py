class Formatter:

    @classmethod
    def format_it(cls, input_string):
        return ''.join([each for each in input_string if each not in ['.', '-']])

