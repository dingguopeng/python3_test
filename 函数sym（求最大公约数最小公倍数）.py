def sym(a, b):
    if a < 1 or b < 1:
        raise TypeError('请输入大于零的数！')
    i = a * b
    if a > b:
        t = a
        a = b
        b = t
    t = 1
    while (t != 0):
        t = a % b
        a = b
        b = t
    j = int(i / a)
    return a, j;

p = int(input('1输入:'))
q = int(input('2输入:'))
print(sym(p, q));
