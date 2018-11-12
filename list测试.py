# -*- coding: utf-8 -*-
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
i = 0
j = 0
while (i < 3):
    j = 0
    while (j < 3):
        print('Hello,', L[i][j], '!')
        j += 1
    i += 1

print([x * x - y for x in range(1, 5) for y in range(1, 5) if  x == y])
