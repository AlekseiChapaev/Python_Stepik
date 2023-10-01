a, b = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

temp = l1 + l2
res = []
i = 0
count = 0
lenght = len(temp)
while i <= lenght-1:
    res.append(str(min(temp)))
    temp.remove(min(temp))
    i +=1
print(' '.join(res))

