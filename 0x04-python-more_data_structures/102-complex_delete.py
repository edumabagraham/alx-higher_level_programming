#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # get the list of keys with dictionary comprehension
    keys = list({i for i, j in a_dictionary.items() if j == value})
    for i in keys:
        del a_dictionary[i]
    return a_dictionary
# Get the value of the keys with a for loop
    # keys=[]
    # for i,j in a_dictionary.items():
    #     if j == value:
    #         keys.append(i)
