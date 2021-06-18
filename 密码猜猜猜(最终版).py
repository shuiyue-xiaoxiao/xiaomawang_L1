import random
print("-- -- -- 密码猜猜猜 -- -- --")
letterList = ["A", "B", "C", "D", "E",
              "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O",
              "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y",
              "Z"]
passwordList = []
while True:
    index = random.randint(0, len(letterList)-1)
    letter = letterList[index]
    
    passwordList.append(letter)
    letterList.pop(index)
    if len(passwordList) == 4:
        break

print("正确密码由四位不重复的大写字母组成，猜猜看呐")
while True:
    posCorrect = 0
    letterCorrect = 0
    user = input("请输入：")
    userList = list(user)
    
    if len(userList) != 4:
        print("别乱输！")
        continue

    if userList == passwordList:
        print("猜对了！")
        break
    else:
        if userList[0] == passwordList[0]:
            posCorrect = posCorrect + 1
        if userList[1] == passwordList[1]:
            posCorrect = posCorrect + 1
        if userList[2] == passwordList[2]:
            posCorrect = posCorrect + 1
        if userList[3] == passwordList[3]:
            posCorrect = posCorrect + 1
        print("位置对：" + str(posCorrect))
        
        if userList[0] in passwordList:
            letterCorrect = letterCorrect + 1
        if userList[1] in passwordList:
            letterCorrect = letterCorrect + 1
        if userList[2] in passwordList:
            letterCorrect = letterCorrect + 1
        if userList[3] in passwordList:
            letterCorrect = letterCorrect + 1
        print("字母对：" + str(letterCorrect))
        
            
        
        

