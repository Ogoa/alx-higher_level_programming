#!/usr/bin/python3
# Function that returns a set of common elements in two sets
def common_elements(set_1, set_2):
    return set(set_1 & set_2)


if __name__ == "__main__":
    common_elements(set_1, set_2)
