#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = 0
    for element in my_list:
        if element > max_value:
            max_value = element
    return max_value
