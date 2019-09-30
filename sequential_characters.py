from string import printable

def all_sequentials(input_string):

    all_chars = printable

    for char in input_string:
        acc = 0
        starting_index = input_string.index(char)
        
        for index, sec_char in enumerate(input_string[starting_index:]):

            
