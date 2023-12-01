#!/usr/bin/python3
count = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(i - 32)}" if count % 2 else f"{chr(i)}", end="")
    count += 1
