#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    prints an integer followed by a new line
    Returns True if value has been correctly printed
    and otherwise False
    Prints in stderr preceeded by Exception
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
