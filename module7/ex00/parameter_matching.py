#!/usr/bin/python3
import sys
import re
# inp = str(input("What was the parameter? "))
# first = sys.argv[1]

# num = len(sys.argv)

if len(sys.argv) == 2:
    first = sys.argv[1]
    inp = str(input("What was the parameter? "))
    if inp == first:
        print("Good job!")
    else:
        print("Nope, sorry...")

else:
    print("none")




