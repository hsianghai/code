# sticks = 21
#
# print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
# print("Whoever will take the last stick will loose")
#
# while True:
#     print("Sticks left: " , sticks)
#     sticks_taken = int(input("Take sticks(1-4):"))
#     if sticks == 1:
#         print("You took the last stick, you loose")
#         break
#     if sticks_taken >= 5 or sticks_taken <= 0:
#         print("Wrong choice")
#         continue
#     print("Computer took: " , (5 - sticks_taken) , "\n")
#     sticks -= 5

print("抢棍子游戏：输入棍子总数，和电脑轮流抢棍子，每次可以取1-4根棍子，每个回合人和电脑共抢5根，拿到最后1根棍子的一方输")

stick = int(eval(input("请输入棍子总数：")))

while True:
    try:
        if stick < 4:
            print("最后" + str(computer_taken) + "根棍子被电脑拿到了，电脑输了")
            break
        else:
            stick_taken = int(eval(input("请输入你要抢的棍子数目（1-4）：")))
            if stick == 1:
                print("你拿到了最后一根棍子，你输了")
                break
            if stick < 5:
                if stick_taken == 4:
                    print("你拿到了最后4根棍子，你输了")
                else:
                    computer_taken = stick - stick_taken
                    print("你抢了" + str(stick_taken) + "根棍子,电脑抢了" + str(computer_taken) + "根棍子,电脑拿到了最后一根棍子，电脑输了")
                    break
            if stick_taken >= 5:
                print("你抢太多棍子啦，请重新输入棍子数目")
                continue
            if stick_taken <= 0:
                print("棍子数目不能为0或负数，请重新输入棍子数目")
                continue
            computer_taken = 5 - stick_taken
            print("你抢了" + str(stick_taken) + "根棍子,电脑抢了" + str(computer_taken) + "根棍子,还剩" + str(stick - 5) + "根棍子")
            print()
        stick -= 5
    except:
        print("你没有抢棍子，请确认")
        continue