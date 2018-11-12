a = int(input("input a :"))
b = int(input("input b :"))
t = 1
k = 3
if (a > b):
    t = a
    a = b
    b = t
while (a <= b):
    if (a % 2 == 0):
        print(a, '不是质数')
    else:
        while (a % k != 0):
            k += 2
            if (k >= a):
                print(a, '是一个质数')
                break
        if (k < a):
            print(a, '不是质数')
    a += 1
