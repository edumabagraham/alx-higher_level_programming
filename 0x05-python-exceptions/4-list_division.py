#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # return [x/y for x in my_list_1 for y in my_list_2]
    new_arr = []
    result = 0
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_arr.append(result)
    return new_arr
