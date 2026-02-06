#!/usr/bin/python3
i = int(input("Enter a number less than 25\n"))

if i > 25:
    print("Error")
elif i == 25:
    print("Error")
else:
    while i <= 25:
        print("Inside the loop, my variable is" + " " +str(i))
        i += 1

    