import random
# 制作棋盘
print("0|1|2")
print("-----")
print("3|4|5")
print("-----")
print("6|7|8")


# 决定先后手
coin = random.randint(0, 1)

chessList = list(range(9))
# 回合数
number = 0
while True:  
    # 依次出子
    number += 1  
    if coin == 0:
        while True:
            user = input("玩家出子：")
            if chessList[int(user)] == int(user):
                chessList[int(user)] = "X"
                coin = 1
                break
            else:
                print("此处有棋子，请重新出子")
    else:
        print("电脑出子：")
        computerDo = 0
        for i in range(9):
            if chessList[i] == i:
                chessList[i] = "X"
                win1 = chessList[0] == chessList[1] == chessList[2]
                win2 = chessList[3] == chessList[4] == chessList[5]
                win3 = chessList[6] == chessList[7] == chessList[8]
                win4 = chessList[0] == chessList[3] == chessList[6]
                win5 = chessList[1] == chessList[4] == chessList[7]
                win6 = chessList[2] == chessList[5] == chessList[8]
                win7 = chessList[0] == chessList[4] == chessList[8]
                win8 = chessList[2] == chessList[4] == chessList[6]
                if win1 or win2 or win3 or win4 or win5 or win6 or win7 or win8:
                    chessList[i] = "O"
                    computerDo = 1
                    coin = 0
                    break
                else:
                    chessList[i] = i

        if computerDo == 0:
            # 电脑随机出子
            while True:
                index = random.randint(0, 8)
                if chessList[index] == index:
                    chessList[index] = "O"
                    coin = 0
                    break

    # 刷新棋盘
    print(str(chessList[0]) + "|" + str(chessList[1]) + "|" + str(chessList[2]))
    print("-----")
    print(str(chessList[3]) + "|" + str(chessList[4]) + "|" + str(chessList[5]))
    print("-----")
    print(str(chessList[6]) + "|" + str(chessList[7]) + "|" + str(chessList[8]))
    #胜利条件
    win1 = chessList[0] == chessList[1] == chessList[2]
    win2 = chessList[3] == chessList[4] == chessList[5]
    win3 = chessList[6] == chessList[7] == chessList[8]
    win4 = chessList[0] == chessList[3] == chessList[6]
    win5 = chessList[1] == chessList[4] == chessList[7]
    win6 = chessList[2] == chessList[5] == chessList[8]
    win7 = chessList[0] == chessList[4] == chessList[8]
    win8 = chessList[2] == chessList[4] == chessList[6]
    # 判断胜负
    if win1 or win2 or win3 or win4 or win5 or win6 or win7 or win8:
        if coin == 1:
            print("玩家获胜！")
        else:
            print("电脑获胜！")
        break
    if number == 9:
        print("和棋")
        break
