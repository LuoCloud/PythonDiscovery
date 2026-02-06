#!/usr/bin/python3
try:
    num_1 = int(input(f"Give me the first number: "))
except ValueError:
    print("Please enter numbers please!")
    
try:
    num_2 = int(input(f"Give me the second number: "))
except ValueError:
    print("Please enter numbers please!")
print("Thank you!")

result_3 = round(num_1 / num_2)

print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} / {num_2} = {result_3}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")

