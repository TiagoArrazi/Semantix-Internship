from source.utils.validator import Validator
from source.utils.validator import Formatter

if __name__ == '__main__':

    opt_dict = {'validate': Validator.validate,
                'format': Formatter.format_it}

    print('OPTIONS -- validate [string], format [string]')

    while True:

        cmd_string = input('>> ')
        cmd_list = cmd_string.split(' ')
        try:
            print(opt_dict[cmd_list[0].lower()](cmd_list[1]))

        except KeyError:
            print('INVALID COMMAND!')

        except ValueError:
            print('INVALID INPUT FORMAT!')



