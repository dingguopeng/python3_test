# 改进打印三角，空心，宽度自设(2 * width - 1)

i = 0
j = 0
t = int(input('input value of width:'))
while (i < t):
    j = i + 1
    while (j > 0):
        print('   ', end=' ')
        j -= 1
    k = (2 * t - 1) - 2 * i
    while (k > 0):
        if (i == 0 or (k == 1 or k == (2 * t - 1) - 2 * i)):
            print(' * ', end=' ')
        else:
            print('   ', end=' ')
        k -= 1
    i = i + 1
    print('')
