#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for i in range(len(matrix)):
        arr.append(matrix[i][i])
    return arr
