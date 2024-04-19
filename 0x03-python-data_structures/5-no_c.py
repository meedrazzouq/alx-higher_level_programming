#!/usr/bin/python3
def no_c(my_string):
    tmp = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            tmp += char
    return tmp
