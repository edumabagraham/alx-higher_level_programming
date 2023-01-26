#!/usr/bin/python3

"""
This is "2-matrix_divided" module
this module contains matrix_divided function divides elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    With list comprehension
    -----------------------
    return [[round(x / div, 2) for x in row] for row in matrix]

    Arguments:
        matrix (list of list): first value to add
        div (int): int that will be used to divide

    List comprehension for the result and regular code for the
    checks
    """

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    if row_size == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]
