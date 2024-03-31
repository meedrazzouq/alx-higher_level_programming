import sys
if len(sys.argv) == 0:
    print("{} argument.".format(len(sys.argv)))
elif len(sys.argv) == 1:
    print("{} argument:".format(len(sys.argv)))
    print("1:", sys.argv[0])
elif len(sys.argv) > 1:
    print("{} arguments:".format(len(sys.argv)))
    for i, arg in enumerate(sys.argv[0:], start=1):
        print("{}:".format(i), arg)
