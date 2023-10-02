count_boys = 4
boys = [1, 4, 6, 2]
count_girls = 5
girls = [5, 1, 5, 7, 9]
boys.sort()
girls.sort()
i = 0
j = 0
count = 0
while i < count_boys and j < count_girls:
    if boys[i] - girls[j] == 0 or abs(boys[i] - girls[j]) == 1:
        count += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1

print(count)