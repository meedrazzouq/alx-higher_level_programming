#!/usr/bin/python3

def add_arg(argv):
    lenarg = len(argv) - 1
    if lenarg == 0:
        print("{:d}".format(lenarg))
        return
    else:
        i = 1
        add = 0
        while i <= lenarg:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
