#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    total = len(argv)

    if total <= 1:
        print("0 arguments.")
    else:
        if total == 2:
            print("{:d} argument:".format(total - 1))
        else:
            print("{:d} arguments:".format(total - 1))
        for i in range(1, total):
            print("{:d}: {:s}".format(i, argv[i]))
