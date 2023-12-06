#!/usr/bin/python3
# Function that returns a set of all elements present in only one set
def only_diff_elements(set_1, set_2):
    return set(set_1 ^ set_2)


if __name__ == "__main__":
    only_diff_elements(set_1, set_2)
