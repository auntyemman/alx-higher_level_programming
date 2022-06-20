#!/usr/bin/python3


def safe_function(fct, *args):
    """
    Executes a function safely and returns a pointer
    to a function
    """

    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
