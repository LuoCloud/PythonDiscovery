 j#!/usr/bin/python3
import sys
import re

# num = len(sys.argv)
lst = str(sys.argv[2:])
result = re.findall("the", lst)
number = len(result)

first = sys.argv[1]
second = sys.argv[2]

if len(sys.argv) != 3:
        print("none")
else:
        if first == second:
                print(number)
        else: 
                print("none")

        
  

       



# if len(sys.argv) == 3:
#         print(number)
    
# else:
#     print("none")