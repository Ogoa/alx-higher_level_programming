#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = len(sys.argv)
    if arguments < 2:
        print("0 arguments.")
    else:
        if arguments == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(arguments - 1))
        for i in range(1, arguments):
            print("{:d}: {:s}".format(i, sys.argv[i]))
