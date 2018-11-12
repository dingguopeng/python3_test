a = int(input("输入被除数:"))
b = int(input("输入除数:"))
i = int(a // b)
j = a % b
if a > b:
    print("结果是:", i, "......", j)
else:
    print("输入错误！")
