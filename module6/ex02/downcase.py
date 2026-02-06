#!/usr/bin/python3
import sys

# print(len(sys.argv))
if (len(sys.argv) != 2):
    print("none")
else:
    string = sys.argv[1]
    print(string.lower())