#!/usr/bin/python3

def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    else:
        for i in range(0, len(str)):
            if i == n:
                char = str[i]
        new_string = str.replace(char, "", 1)
    return new_string

# def remove_char_at(str, n):
#     new_string = ""

#     for i in range(len(str)):
#         if i != n:
#             new_string += str[i]
#     return new_string
