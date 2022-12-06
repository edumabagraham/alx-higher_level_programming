#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for element in item:
            if item.index(element) != len(item) - 1:
                print("{:d}".format(element), end=' ')
            else:
                print("{:d}".format(element), end='')
        print("")
