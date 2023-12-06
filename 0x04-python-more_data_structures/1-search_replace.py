#!/usr/bin/python3
# Function that replaces all occurrences of an element by another in a new list
def search_replace(my_list, search, replace):
    for i in range(my_list.count(search)):
        idx = my_list.index(search)
        my_list = my_list[:idx] + [replace] + my_list[idx + 1:]
    return my_list


if __name__ == "__main__":
    search_replace(my_list, search, replace)
