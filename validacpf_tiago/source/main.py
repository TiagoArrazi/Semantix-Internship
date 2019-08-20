from source.utils.validator import Validator

if __name__ == '__main__':

    opt_dict = {'validate': Validator.validate,
                'format': Validator.format_}

    print('OPTIONS -- validate [string], format [string]')

    while True:

        try:
            cmd_string = input('>> ')
            cmd_list = cmd_string.split(' ')
            print(opt_dict[cmd_list[0].lower()](cmd_list[1]))

        except KeyError:
            print('INVALID COMMAND!')

        except ValueError:
            print('INVALID INPUT FORMAT!')

        except KeyboardInterrupt:
            exit(0)



