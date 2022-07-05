#!/usr/bin/python3

"""This module defines a class "Student" """


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of a specified
        attribute"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for atr in attrs:
            try:
                new_dict[atr] = self.__dict__[atr]
            except BaseException:
                pass
        return new_dict
