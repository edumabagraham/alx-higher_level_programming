#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    list_of_squares = [[i * i for i in element] for element in matrix]
    return list_of_squares
    # list_of_squares = []
    # for i in matrix:
    #     squared_list = list(map(lambda x: x * x, i))
    #     list_of_squares.append(squared_list)
    # return list_of_squares
