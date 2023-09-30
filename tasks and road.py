count_tasks = 3
time_to_road = 222
count = 0
while (time_to_road <= 240) and count <= count_tasks:
    count += 1
    time_to_road = time_to_road + count * 5
print(count-1)