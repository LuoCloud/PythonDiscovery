#!/usr/bin/python3
# first_number = round(float(input("Enter the first number:\n")))
# second_number = round(float(input("Enter your second number:\n")))
# result = round(first_number * second_number)

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter your second number:\n"))
result = int(first_number * second_number)

print(f"{first_number} x {second_number} = {result}")

if result == 0:
    print("The result is both positive and negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is negative.")