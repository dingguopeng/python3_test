def jiecheng(x):
    if not isinstance(x,(int)):
        raise TypeError('输入的值有误')
    if x == 0:
        return 1
    else:
        return jiecheng(x-1)*x
s = int(input('输入一个自然数：'))
print(s,'的阶乘是：',jiecheng(s))