number1 = int(input("输入第一个数字："))
number2 = int(input("输入第二个数字："))
number3 = int(input("输入第三个数字："))
print(int((number1 + number2 + number3) / 3))

N = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))