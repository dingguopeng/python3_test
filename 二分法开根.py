i = int(input("输入一个数："))
max = i
min = 0
mid = max + min / 2
k = 1
while k < 20:
    if mid ** 2 > i:
        max = mid
        mid = (max + min) / 2
    else:
        min = mid
        mid = (max + mid) / 2
    k += 1
print('近似值：',mid)