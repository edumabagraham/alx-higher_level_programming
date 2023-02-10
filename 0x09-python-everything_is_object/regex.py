#!/usr/bin/python3

import re
def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
    
    
    # YOUR CODE HERE
    # # print(grades)
    # grades_str = ""
    # grades_str = grades
    # # print(type(grades_str))
    # grades_str = re.findall(".*:B",grades_str)
    # grades_str = "".join(grades_str)
    grades_with_names = re.findall(".*: B",grades)
    # grades_str.pop()
    # return grades_str
    # grades = re.findall(".*:B",grades)
    
    
    # if re.search(".*:B",grades):
    #     print("found")
    return grades_with_names
    raise NotImplementedError()
print(grades())
