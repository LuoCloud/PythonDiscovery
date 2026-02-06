#!/usr/bin/python3
# first_arr = [0, 2, 5, 7, 5, -10, -20, -6]
# lst = [x for x in first_arr if x > 5]
# sec_arr = [x +2 for x in lt]

# print(first_arr)
# print(sec_arr)

# first_arr = [0, 2, 5, 7, 5, -10, -20, -6]
# remov = []

# for x in first_arr:
#     if x not in remov:
#         remov.append(x)

# print(first_arr)

# first_arr = [0, 2, 5, 7, 5, -10, -20, -6]
# lst = list(set(first_arr))
# print(first_arr)

first_arr = [2, 8, 9, 48, 8, 22, -12, 2]
# first_arr = list( dict.fromkeys(first_arr) )
# lst = [x for x in first_arr if x > 5]
# sec_arr = [x +2 for x in lst]
# print(sec_arr)
lst = [x for x in first_arr if x > 5]
sec_arr = set([x +2 for x in lst])

print(first_arr)
print(sec_arr)