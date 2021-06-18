import random
print("-- -- -- 欢迎来到歌王争霸赛 -- -- --")
print("规则：每一题可选择歌词中隐藏的字数，答对后根据隐藏的字数给分")
user = input("请输入挑战者姓名：")

songs = ["稻香-周杰伦", "魔法城堡-TFBOYS",
         "光年之外-邓紫棋", "李白-李荣浩"]
lyrics = ["还记得你说家是唯一的城堡",
          "传说中魔法的城堡守护每个微笑",
          "缘分让我们相遇乱世之外",
          "要是能重来我要选李白"]
score = 0
for i in range(4):
    song = songs[i]
    lyric = lyrics[i]
    print("第" + str(i+1) + "首：" + song + ",共" + str(len(lyric)) + "个字")

    hideNum = input("请输入隐藏的字数：")
    lyricList = list(lyric)

    idxList = list(range(len(lyric)))
    for j in range(int(hideNum)):
        a = random.randint(0, len(idxList) - 1)
        idx = idxList.pop(a)
        lyric = lyric[0: idx] + "*" + lyric[idx + 1: len(lyric)]

    print(lyric)

    answer = input("请输入正确的歌词：")
    if answer == lyric[i]:
        score += int(hideNum)
        print("当前得分：" + str(score))
print("挑战结束，" + user + "的最终得分：" + str(score))
