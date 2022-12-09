#!/usr/bin/python3

import re


def odd(num):
    if num % 2:
        return True
    else:
        return False

def map_func(odd, list):
    odd_list = []
    for i in list:
        if odd(i):
            odd_list.append(i)
    return odd_list

print(map_func(odd, [1,2,3,4,5,6,7,8,9])) 