#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squareMatrix = []

    for x in matrix:
        squareMatrix.append(list(map((lambda x: x**2), x)))
    return squareMatrix
