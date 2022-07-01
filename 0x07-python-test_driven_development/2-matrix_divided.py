#!/usr/bin/python3
"""
matrix division.
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for line in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), line)))
    return (new_matrix)
