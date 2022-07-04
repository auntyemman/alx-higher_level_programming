#!/usr/bin/python3
"""This module contains a class BaseGeometry and subclass Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A representation of a square."""

    def __init__(self, size):
        """Instantiation of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
