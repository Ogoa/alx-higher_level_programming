#!/usr/bin/python3
# Function that finds the biggest integer of a list
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest = -1
    for i in my_list:
        if i > largest:
            largest = i
    return largest


if __name__ == "__main__":
    max_integer(my_list)
