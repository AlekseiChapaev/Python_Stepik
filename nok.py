a, b = map(int, input().split())
temp_a = a
temp_b = b
while temp_b > 0:
    c = temp_a % temp_b
    temp_a = temp_b
    temp_b = c
nod = temp_a
nok = int((a * b) / nod)

print(nok)