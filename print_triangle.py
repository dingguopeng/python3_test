print('   ')

i = 0
j = 0
while (i < 9):
    j = i + 1
    while (j > 0):
        print('   ', end=' ')
        j -= 1
    k = 17 - 2*i
    while (k > 0):
        print(' * ', end=' ')
        k -= 1
    i = i + 1
    print('')
