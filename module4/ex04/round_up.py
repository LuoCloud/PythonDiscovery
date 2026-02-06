#!/usr/bin/python3
# number  = float(input("Give me a number: "))
# print(round(number,0))
import math

num = float(input("Give me a number: "))

if num.is_integer():
    print(int(num))
else:
    print(math.ceil(num))

