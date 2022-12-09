#!/usr/bin/python3

def best_score(a_dictionary):
    # if a_dictionary is None:
    #     return None
    # else:
    #     key = list(a_dictionary.values())
    #     max_value = key[0]
    #     max_key = None
    #     for i, j in a_dictionary.items():
    #         if j > max_value:
    #             max_value = j
    #             max_key = i
    #     return (max_key)
    if not a_dictionary:
        return None
    return max(a_dictionary, key=lambda x: a_dictionary[x])
