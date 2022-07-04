#!/usr/bin/python3
''' module: 2-is_same_class
'''


def is_kind_of_class(obj, a_class):
    '''function: is_kind_of_class
    obj: an object
    a_class: a class
    Returns: Bool
    '''

    if isinstance(obj, a_class):
        return True
    return False
