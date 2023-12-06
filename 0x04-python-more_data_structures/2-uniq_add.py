#!/usr/bin/python3
# Function that adds all unique integers in a list
def uniq_add(my_list=[]):
    total = 0
    a = set(my_list)
    for i in a:
        total = total + i
    return total


if __name__ == "__main__":
    uniq_add(my_list)
