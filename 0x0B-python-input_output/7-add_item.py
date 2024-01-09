#!/usr/bin/python3
'''A script that adds all arguments to a Python list and then
saves them to a file'''
import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    '''Adds all arguments to a Python list'''

    filename = "add_item.json"
    existing_list = []
    new_list = []
    i = 1

    try:
        existing_list = list(load_from_json_file(filename))
    except FileNotFoundError:
        with open(filename, "w") as f:
            json.dump("[]", f)

    while i < len(sys.argv):
        new_list.append(str(sys.argv[i]))
        i += 1

    existing_list += new_list
    save_to_json_file(existing_list, filename)


if __name__ == "__main__":
    main()
