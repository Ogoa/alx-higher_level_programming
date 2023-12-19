#!/usr/bin/python3
# Function that divides 2 intgers and prints the result
def safe_print_division(a, b):
    quotient = 0.0
    try:
        quotient = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient


if __name__ == "__main__":
    safe_print_division(a, b)
