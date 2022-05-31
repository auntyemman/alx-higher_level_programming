#!/usr/bin/python3

nc = 0
for x in range(122, 96, -1):
    if x % 2 == 0:
        nc = x
    else:
        nc = x - 32
    print("{}".format(chr(nc)), end='')
