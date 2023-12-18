#!/usr/bin/python3
# Function that prints an integer
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True


if __name__ == "__main__":
    safe_print_integer_err(value)
