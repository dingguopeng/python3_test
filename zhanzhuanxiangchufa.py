a = int(input("input a :"))
b = int(input("input b :"))
t = a
if (a > b):
    t = a
    a = b
    b = t
k = a * b
while (t != 0):
    t = a % b
    a = b
    b = t

print('最大公约数为', a)
print('最小公倍数为', int(k/a))
