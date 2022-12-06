#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list:
        if 0 <= idx < len(my_list):
            copy_of_list = my_list[:]
            copy_of_list[idx] = element
            return copy_of_list
        return my_list
