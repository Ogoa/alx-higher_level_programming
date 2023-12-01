#!/usr/bin/python3
count = 0
for i in range(ord('z'), ord('a') - 1, -1):
    if count % 2:
        print(f"{chr(i - 32)}", end="")
    else:
        print(f"{chr(i)}", end="")
    count += 1
