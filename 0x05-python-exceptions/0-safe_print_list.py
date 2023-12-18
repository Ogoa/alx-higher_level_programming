#!/usr/bin/python3
# Function that prints x elements of a list
def safe_print_list(my_list=[], x=0):
    total_printed = 0
    i = 0

    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            total_printed = total_printed + 1
            i = i + 1
        except IndexError:
            break

    print("")
    return total_printed


if __name__ == "__main__":
    safe_print_list(my_list, x)
