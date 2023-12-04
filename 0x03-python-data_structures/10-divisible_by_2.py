#!/usr/bin/python3
# Finds all multiples of 2 in a list
def divisible_by_2(my_list=[]):
    multiples = []
    for i in my_list:
        if i % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return multiples


if __name__ == "__main__":
    divisible_by_2(my_list)
