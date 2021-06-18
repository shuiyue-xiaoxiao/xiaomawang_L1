import random

print("----- 欢迎来到千词斩 -----")

questionList = ["随机", "错误", "继续", "硬币", "答案",
                "如果", "否则", "打印", "输入", "问题"]
answerList = ["random", "error", "continue", "coin", "answer",
              "if", "else", "print", "input", "question"]
count = 0
while True:
    index = random.randint(0, len(questionList) - 1)
    question = questionList[index]
    if question == None:
        continue
    
    answer = answerList[index]
    
    user = input("请问 " + question + " 的英文单词是：")

    if user == answer:
        count = count + 1
        if count == 10:
            print("太棒了，你背下了所有的单词！")
            break
        questionList[index] = None
        print("**** 恭喜你，答对了 ****")
    else:
        print("**** 哎呀，答错了 ****")
