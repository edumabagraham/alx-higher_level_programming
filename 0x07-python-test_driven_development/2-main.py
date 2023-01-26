#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided



# Division by 0

# print("--------------------------")
# matrix = [[7.8, 8.7, 4.9], [9.3,10.78,3.2]]
# print(matrix_divided(matrix, 0))
# print(matrix)

# Matrix not a list
# print("--------------------------")
# matrix = ([7.8, 8.7, 4.9], [9.3,10.78,3.2])
# print(matrix_divided(matrix, 2))
# print(matrix)

# List of non-list
# print("--------------------------")
# matrix = [(7.8, 8.7, 4.9), [9.3,10.78,3.2]]
# print(matrix_divided(matrix, 2))
# print(matrix)

# print("--------------------------")
# matrix = [[7.8, 8.7, 4.9], (9.3,10.78,3.2)]
# print(matrix_divided(matrix, 2))
# print(matrix)

# print("--------------------------")
# matrix = [(7.8, 8.7, 4.9), (9.3,10.78,3.2)]
# print(matrix_divided(matrix, 2))
# print(matrix)

# List of list of non integers and floats
# print("--------------------------")
# matrix = [[7.8, "Student", 4.9], [9.3,10.78,3.2]]
# print(matrix_divided(matrix, 2))
# print(matrix)

# print("--------------------------")
# matrix = [[7.8, "Student", 4.9], [9.3,10.78,"Student"]]
# print(matrix_divided(matrix, 2))
# print(matrix)

# Matrix of uneven row size
# print("--------------------------")
# matrix = [[1, 2],[4, 5, 3]]
# print(matrix_divided(matrix, 3))
# print(matrix)

# print("--------------------------")
# matrix = [[1, 2, 3],[4, 5]]
# print(matrix_divided(matrix, 3))
# print(matrix)

print("--------------------------")
matrix = [[1, 3, 4], [1, 2, 3]]
print(matrix_divided(matrix, 16))
print(matrix)
