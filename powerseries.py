x = float(input("请输入x的值："))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.001:
        break
print("循环次数= {} and 计算结果= {}".format(n, result))