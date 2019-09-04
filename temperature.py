c = int(input("请输入摄氏温度："))
print("您所输入的摄氏温度为：" + str(c))
print("是否转化为华氏温度？是：1，否：0")
submit = int(input())
if submit == 1:
    print(str(c) + "℃转化为华氏温度为：" + str(9 * c / 5 + 32) + "℉")
else:
    print("不转化")

f = int(input("请输入华氏温度："))
print("您所输入的摄氏温度为：" + str(f))
print("是否将华氏温度转化为摄氏温度？是：1，否：0")
if submit == 1:
    print(str(f) + "℉转化为摄氏温度为：" + str(5 * (f - 32) / 9) + "℉")
else:
    print("不转化")

fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 转换为摄氏度
    print("{:5d} {:7.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 25
