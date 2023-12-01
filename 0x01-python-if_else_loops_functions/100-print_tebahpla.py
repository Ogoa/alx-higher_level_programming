#!/usr/bin/python3
count = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - 32) if count % 2 else chr(i)), end="")
    count += 1
