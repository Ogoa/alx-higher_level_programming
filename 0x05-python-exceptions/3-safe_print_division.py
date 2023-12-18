#!/usr/bin/python3
# Function that divides 2 intgers and prints the result
def safe_print_division(a, b):
    quotient = 0.0
    try:
        quotient = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(quotient if quotient else None))
        return quotient


if __name__ == "__main__":
    safe_print_division(a, b)
