#!/usr/bin/python3
# Function that prints a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(list(a_dictionary))
    for i in sorted_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary)
