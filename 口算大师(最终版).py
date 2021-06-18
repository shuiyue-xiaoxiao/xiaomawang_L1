import random
print("-- -- -- -- 口算大师 -- -- -- --")
while True:
    coin = random.randint(1, 4)
    if coin == 1:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = a + b
        user = input(str(a) + " + " + str(b) + " = ")
        if str(c) == user:
            print("恭喜你，答对了")
        else:
            print("答错了，加油哦")
    elif coin == 2:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = a - b
        user = input(str(a) + " - " + str(b) + " = ")
        if str(c) == user:
            print("恭喜你，答对了")
        else:
            print("答错了，加油哦")
    elif coin == 3:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = a * b
        user = input(str(a) + " * " + str(b) + " = ")
        if str(c) == user:
            print("恭喜你，答对了")
        else:
            print("答错了，加油哦")
    elif coin == 4:
        a = random.randint(0, 10)
        b = random.randint(1, 10)
        c = round(a / b, 2)
        user = input(str(a) + " / " + str(b) + " = (最多保留两位小数,整除请加.0)")
        if str(c) == user:
            print("恭喜你，答对了")
        else:
            print("答错了，加油哦")
