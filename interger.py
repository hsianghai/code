days = int(input("Enter days: "))
months = days // 30
days = days % 30
print("Months = {} Days = {}".format(months, days))
print("Months = {} Days = {}".format(*divmod(days, 30)))
print(str(days))