#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list.copy()
    if idx < 0:
        return tmp
    elif idx >= len(my_list):
        return tmp
    tmp[idx] = element
    return tmp
