#!/usr/bin/python3
# Function that returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary)
    return {i: a_dictionary[i] * 2 for i in keys}


if __name__ == "__main__":
    multiply_by_2(a_dictionary)
