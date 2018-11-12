def pingfanghe(para):
    if not para:
        return 0
    s = 0
    for i in para:
        s += int(i) ** 2
    return s


j = 0
l = []
while (j <= 5):
    l.append(j)
    j += 1
print(pingfanghe(l))
print(*l)
