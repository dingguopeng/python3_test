def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

s = float(input('输入一个数：'))
print('该数的绝对值是：',my_abs(s))