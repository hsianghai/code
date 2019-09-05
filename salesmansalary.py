base_salary = 1500
bonus_rate = 200
rate = 0.02
num = int(input("请输入售卖的相机数目:"))
price = float(input("请输入相机的价格："))
final_salary = base_salary + bonus_rate * num + price * rate * num
print("最终工资是:" + str(final_salary) )
