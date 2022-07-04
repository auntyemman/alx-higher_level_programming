#!/usr/bin/python3

"""This module contains the function `inherits_from`"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class\
        that inherited from  a_class ; otherwise False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
