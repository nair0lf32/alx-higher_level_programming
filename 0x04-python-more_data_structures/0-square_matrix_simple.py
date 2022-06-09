#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for i in matrix:
        arr.append(list(map(lambda j: j * j, i)))
    return arr
