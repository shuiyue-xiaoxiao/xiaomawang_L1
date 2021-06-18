import random
print("-- -- -- 卡牌对决 -- -- --")
card1 = {"名称":"诺兹多姆", "攻击力":5000, "防御力":4000, "敏捷":40, "攻击距离":2}
card2 = {"名称":"阿莱克斯塔萨", "攻击力":3000, "防御力":2000, "敏捷":60, "攻击距离":3}
card3 = {"名称":"伊瑟拉", "攻击力":2000, "防御力":6000, "敏捷":30, "攻击距离":4}
card4 = {"名称":"玛里苟斯", "攻击力":2000, "防御力":4000, "敏捷":50, "攻击距离":4}
card5 = {"名称":"耐萨里奥", "攻击力":6000, "防御力":2000, "敏捷":20, "攻击距离":2}
print("""规则：
1、双方初始血量：10000
2、对决之前，双方随机获得3张卡牌
3、每回合双方派出1张卡牌出战，对决后，出战卡牌消失，并重新抽取1张卡牌
4、敏捷高的一方进行攻击，对方根据自身卡牌的防御力，扣除血量
5、接着敏捷低的一方进行反击，对方根据自身卡牌的防御力，扣除血量
6、血量低于0的一方输掉比赛
""")

# 血量
playerHP = 10000
enemyHP = 10000
# 卡池
cards = [card1, card2, card3, card4, card5]
# 抽取卡牌
playerCards = []
enemyCards = []
for i in range(3):
    a = random.randint(0, len(cards) - 1)
    playerCards.append(cards[a])
    b = random.randint(0, len(cards) - 1)
    enemyCards.append(cards[b])
while True:
    # 卡牌展示
    print("我方卡牌：")
    for i in playerCards:
        print(i)
    # 我方出牌
    playerSelect = input("派第几张卡牌出战：")
    playerC = playerCards[int(playerSelect) - 1]
    print("我方派出了：" + playerC["名称"])
    # 敌方出牌
    enemySelect = random.randint(0, len(enemyCards) - 1)
    enemyC = enemyCards[enemySelect]
    print("敌方派出了：" + enemyC["名称"])

    # 我方先攻击
    if playerC["敏捷"] > enemyC["敏捷"]:
        print("我方发起攻击！")
        playerHurt = playerC["攻击力"] - enemyC["防御力"]
        if playerHurt < 0:
            playerHurt = 0
        enemyHP = enemyHP - playerHurt
        if enemyHP <= 0:
            print("对决结束，敌方血量为0，我方获胜！")
            break
        else:
            print("我方造成伤害：" + str(playerHurt) + "，敌方剩余血量：" + str(enemyHP))
        # 敌方反击
        if enemyC["攻击距离"] >= playerC["攻击距离"]:
            print("敌方发起反击！")
            enemyHurt = enemyC["攻击力"] - playerC["防御力"]
            if enemyHurt < 0:
                enemyHurt = 0
            playerHP = playerHP - enemyHurt
            if playerHP <= 0:
                print("对决结束，我方血量为0，敌方获胜！")
                break
            else:
                print("敌方造成伤害：" + str(enemyHurt) + "，我方剩余血量：" + str(playerHP))
    # 敌方先攻击
    elif playerC["敏捷"] < enemyC["敏捷"]:
        print("敌方发起攻击！")
        enemyHurt = enemyC["攻击力"] - playerC["防御力"]
        if enemyHurt < 0:
            enemyHurt = 0
        playerHP = playerHP - enemyHurt
        if playerHP <= 0:
            print("对决结束，我方血量为0，敌方获胜！")
            break
        else:
            print("敌方造成伤害：" + str(enemyHurt) + "，我方剩余血量：" + str(playerHP))
        # 我方反击
        if playerC["攻击距离"] >= enemyC["攻击距离"]:
            print("我方发起反击！")
            playerHurt = playerC["攻击力"] - enemyC["防御力"]
            if playerHurt < 0:
                playerHurt = 0
            enemyHP = enemyHP - playerHurt
            if enemyHP <= 0:
                print("对决结束，敌方血量为0，我方获胜！")
                break
            else:
                print("我方造成伤害：" + str(playerHurt) + "，敌方剩余血量：" + str(enemyHP))
    # 不攻击
    else:
        print("对方跑得太快，追不上！")

    # 删除卡牌
    playerCards.remove(playerC)
    enemyCards.remove(enemyC)
    # 补充卡牌
    a = random.randint(0, len(cards) - 1)
    playerCards.append(cards[a])
    b = random.randint(0, len(cards) - 1)
    enemyCards.append(cards[b])

    # 魔法泉
    spring = random.randint(1, 100)
    if spring <= 30:
        print("魔法泉发动！")
        magic = random.randint(1, 100)
        if magic <= 50:
            print("攻击力低于3000的卡牌获得 泰坦祝福")
            for i in cards:
                if i["攻击力"] < 3000:
                    i["buff"] = "泰坦祝福"
        else:
            print("攻击力高于6000的卡牌受到 混沌侵蚀")
            for i in cards:
                if i["攻击力"] > 6000:
                    i["buff"] = "混沌侵蚀"
    else:
        print("魔法泉很安静！")

    # buff
    for i in cards:
        if "buff" in i:
            if i["buff"] == "泰坦祝福":
                i["攻击力"] += 1000
            elif i["buff"] == "混沌侵蚀":
                i["攻击力"] -= 1000
                if i["攻击力"] < 0:
                    i["攻击力"] = 0
