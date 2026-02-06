#!/usr/bin/python3
import sys
lst = sys.argv[1:]

if len(sys.argv) == 1:
    print("none")
else:
    num = len(sys.argv)-1
    print("parameters: ",num)


    words = len(lst)
    for i in lst:
        print(f"{i}: {len(i)}")
         
   
 