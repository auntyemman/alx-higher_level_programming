#!/usr/bin/python3

"""This module contains the function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
