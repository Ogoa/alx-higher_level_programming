#!/usr/bin/python3
# Function that prints the first x elements of a list and only integers
# Returns the real number of integers printed
def safe_print_list_integers(my_list=[], x=0):
    total_printed = 0
    i = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            total_printed = total_printed + 1
        except IndexError as e:
            raise
        except (TypeError, ValueError):
            pass
        i = i + 1

    print("")
    return total_printed


if __name__ == "__main__":
    safe_print_list_integers(my_list, x)
