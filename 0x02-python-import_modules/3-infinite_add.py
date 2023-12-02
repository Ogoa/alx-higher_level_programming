#!/usr/bin/python3
import sys

def sum_of_arguments():
    args = len(sys.argv)
    total = 0
    if args < 2:
        return 0
    else:
        for i in range(1, args):
            total += int(sys.argv[i])
        return total

if __name__ == "__main__":
    print(sum_of_arguments())
