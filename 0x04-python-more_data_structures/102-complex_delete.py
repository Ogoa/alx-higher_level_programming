#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary)
    for i in keys:
        if a_dictionary.get(i) == value:
            del a_dictionary[i]
    return a_dictionary


if __name__ == "__main__":
    complex_delete(a_dictionary, value)
