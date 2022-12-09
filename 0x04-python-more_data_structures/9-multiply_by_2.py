#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    a_dictionary_times_2 = {x: y*2 for (x, y) in a_dictionary.items()}
    return a_dictionary_times_2
