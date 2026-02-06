#!/usr/bin/python3
# try:
#     num_int = int(input(f"Give me a number: ")) 
#     print("This is an integer.")

# except ValueError:
#     print("This number is a decimal.")

num = float(input("Give me a number: "))

if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")

