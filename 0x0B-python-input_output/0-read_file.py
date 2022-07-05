#!/usr/bin/python3

"""This module defines the function read_file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
