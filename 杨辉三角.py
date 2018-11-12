l = [x for x in range(1, 10)]
s = []
for i in range(1, 10):
    for j in range(0, i):
        if j == 0 or j == i-1:
            s[i-1][j-1] = 1
        else:
            s[i-1][j-1] = s[i - 2][j-1] + s[i - 2][j - 2]
        print(s[i-1][j-1],)

