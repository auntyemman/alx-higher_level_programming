#!/usr/bin/python3

"""This module contains the function append_write"""


def append_write(filename="", text=""):
    """Append a string to the end of the text file (UTF8) and
    returns the number of characters added."""

    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
