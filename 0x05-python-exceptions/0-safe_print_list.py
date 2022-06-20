#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ A function that prints x elements of a list """
    length = 0
    for index in range(x):
        try:
            position = my_list[index]
            print(position, end='')
            length += 1
        except Exception as error:
            break
    print('')
    return length
