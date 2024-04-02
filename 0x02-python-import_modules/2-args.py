#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1  # Number of arguments excluding the script name

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
    print("1:", sys.argv[1])
else:
    print(f"{num_args} arguments:")
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
