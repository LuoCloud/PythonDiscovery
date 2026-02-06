#!/usr/bin/python3
import sys


# a = int(sys.argv[1])
# b = int(sys.argv[2])
argv = sys.argv[1:]

if len(sys.argv) != 3:
    print("none")

else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if a < b:
        rang = range(a,b+1)
        lst = list(rang)
        print(lst)
    else:
        print("none")


