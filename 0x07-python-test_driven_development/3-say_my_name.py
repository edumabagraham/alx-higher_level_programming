#!/usr/bin/python3
"""
This module contains a function that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    first_name: first argument
    last_name: last argument
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
