#!/usr/bin/python3
import sys

num = len(sys.argv)
lst = sys.argv[1:]


# rem = del.sys.argv[1]

# print(num)

if num > 2:
    for lst in reversed(lst):
        print(lst)
    
else:
    print("none")


     