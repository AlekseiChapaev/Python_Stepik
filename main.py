# num = int(input())
# while int(str(num)[0]) != 1 and num < 1000000000:
#     num *= int(str(num)[0])
# print(num)

# print(sum(map(int, iter(input, '0'))))

# t = []
# while 0 not in t:
#     t.append(int(input()))
# print(sum(t))

# s = input()
# temp = ''
# while 4 < len(s) < 10:
#     temp = s
#     s = input()
# print(temp)

v = int(input())
tempSum = 0
tempCount = 0
sum = 0
count = 0
while v >= tempSum:
    tempSum += int(input())
    tempCount += 1
    if tempSum < v:
        sum = tempSum
        count = tempCount
print('Довольно')
print(sum)
print(count)
