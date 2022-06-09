#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for i in matrix:
        arr.append(list(map(lambda x: x * x, i)))
    return arr
