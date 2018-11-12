# 求解方程的根，并能接受多次计算
import math

flag = 1
while (flag):
    a = float(input("input a : "))
    b = float(input("input b : "))
    c = float(input("input c : "))

    if (a != 0 and (b ** 2 - 4 * a * c >= 0)):
        print('x1 = ', (0 - b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        print('x2 = ', (0 - b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    elif (a == 0):
        print('a = 0')
    else:
        print('无实根')
    while (1):
        flag = input('continue?  Y/N : ')
        if (flag == 'Y' or flag == 'y'):
            flag = 1
            break
        elif (flag == 'N' or flag == 'n'):
            flag = 0
            break
        else:
            print('please check the value of input')
