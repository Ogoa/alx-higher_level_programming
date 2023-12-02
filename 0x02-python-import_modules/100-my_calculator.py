#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def operations(a, b, operator):
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        return 0
    return 1


if __name__ == "__main__":
    argv = sys.argv
    args = len(argv)
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if operations(int(argv[1]), int(argv[3]), argv[2]) == 0:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
