#!/usr/bin/python3
for i in range(0, 99 + 1):
    print("{:02d}".format(i), end="")
    print("{}".format(", " if i < 99 else "\n"), end="")
