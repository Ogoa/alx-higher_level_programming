#!/usr/bin/python3
# Function that prints an integer
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    safe_print_value(value)
