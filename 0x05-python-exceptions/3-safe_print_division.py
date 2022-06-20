#!/usr/bin/python3
def safe_print_division(a, b):
    """  A function that divides 2 integers and prints the result """
    try:
        division = a / b
    except:
        division = None       
    finally:
        print("Inside result: {}". format(division))
        return division
