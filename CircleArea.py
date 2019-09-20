import  math
radius = float(input("输入圆的半径:"))
area = math.pi * radius * radius
print("圆的面积是：" + str("{:.5f}".format(area)))