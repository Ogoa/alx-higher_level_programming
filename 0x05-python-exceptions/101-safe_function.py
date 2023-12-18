#!/usr/bin/python3
import sys


# Function that executes a function safely
def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None


if __name__ == "__main__":
    safe_function(fct, args)
