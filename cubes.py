cubes_quantity = int(input())
top = 1
count = 0
i = 0
while cubes_quantity - count >= 0:
    top = i * (i + 1) / 2
    count += top
    i += 1
print(i-2)