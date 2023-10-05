a = 345
b = 555

# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

while b > 0:
    c = a % b
    a = b
    b = c
print(a)