#!/usr/bin/python3

def open_file():
    try:
        with open('file.txt') as file:
            read_data = file.read()
            print(read_data)
    except FileNotFoundError as fnf_err:
        print(fnf_err)   
    else:
        print("**Success**")
open_file()