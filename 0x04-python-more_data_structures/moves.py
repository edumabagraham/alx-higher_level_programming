#!/usr/bin/python3



# def minimumMoves(arr1, arr2):
#     array1 = broken_arr(arr1)
#     array2 = broken_arr(arr2)
#     moves = 0
#     for i in range(0, len(array1)):
#         if int(array1[i]) < int(array2[i]):
#             moves += int(array2[i]) - int(array1[i])
#         elif int(array1[i]) > int(array2[1]):
#             moves += int(array1[i]) - int(array2[i])
#     print(moves)

# def broken_arr(arr):
#     all_arr1 = []
#     for i in arr:
#         for j in str(i):
#             all_arr1.append(j)
#     return (all_arr1)


# arr1 = [1234,4321]
# arr2 = [2345,3214]
# minimumMoves(arr1, arr2)








# str_arr1 = [str(i) for i in arr1]
# str_arr2 = [str(i) for i in arr2]
# # print(str_arr1, str_arr2)

# for i in range (0, len(arr1)):
#     print(i)


# def counts(teamA, teamB):
#     # Write your code here
#     arr = []
#     for i in teamB:
#         count = 0
#         for j in teamA:
#             if j <= i:
#                 count += 1
#         arr.append(count)
#     return arr

# teamA = [2, 10, 5, 4, 8]
# teamB = [3, 1, 7, 8]
# print(counts(teamA,teamB))

def counts(teamA, teamB):
    i = 0
    new_list = [i for j in teamB for k in teamA if k <= j]
    return new_list

teamA = [2, 10, 5, 4, 8]
teamB = [3, 1, 7, 8]
print(counts(teamA,teamB))