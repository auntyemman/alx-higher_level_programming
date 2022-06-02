#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    total = len(argv) - 1

    if total <= 1:
        print("0 arguments.")
    else:
        if total == 2:
            print("{:d} argument:".format(total))
        else:
            print("{:d} arguments:".format(total))
        for i in range(1, total + 1):
            print("{:d}: {}".format(i, argv[i]))
