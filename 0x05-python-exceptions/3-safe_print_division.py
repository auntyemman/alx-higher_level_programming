#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result
    The result of division should print on Finally
    Returns Value of division, otherwise None
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))

        return result
