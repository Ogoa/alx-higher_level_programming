#!/usr/bin/python3
# Function that returns a key with the biggest integer value
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest = -1
    key = ""
    for i in list(a_dictionary):
        if a_dictionary[i] > largest:
            largest = a_dictionary[i]
            key = i
    return key


if __name__ == "__main__":
    best_score(a_dictionary)
