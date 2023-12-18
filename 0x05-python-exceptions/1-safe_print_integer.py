#!/usr/bin/python3
# Function that prints an integer
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    safe_print_value(value)
