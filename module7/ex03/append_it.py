#!/usr/bin/python3
import sys
lst = sys.argv[1:]

if len(lst) == 0:
    print("none")
else:
    for items in lst:
        if items.find("ism",len(items)-3):
            continue
        else:
            print(items + "ism")





