#!/usr/bin/python3
def safe_print_integer(value):
    """ A  function that prints an integer with"""
    while value:
        try:
            print("{:d}".format(value))
            return True
        except ValueError:
            return False
