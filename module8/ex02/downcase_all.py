#!/usr/bin/python3
import sys

def downcase_it(lst):
        return lst.lower()

num = len(sys.argv)
lst = sys.argv[1:]

if num == 1:
    print("none")
else:
    for text in lst:
        print(downcase_it(text))
    



