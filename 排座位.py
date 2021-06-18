import random
print("-- -- 排座位 -- --")
print("输入：结束 - 完成输入")
print("输入：修改 - 修改姓名")
print("输入：删除 - 删除姓名")

names = []
while True:
    user = input("请输入学生姓名：")
    if user == "结束":
        break
    elif user == "修改":
        oldName = input("请输入需要修改的学生姓名：")
        if oldName in names:
            idx = names.index(oldName)
            newName = input("请输入更新的姓名：")
            names[idx] = newName
            print(oldName + "已修改为：" + newName)
        else:
            print(oldName + "不存在！")
    elif user == "删除":
        oldName = input("请输入需要删除的学生姓名：")
        if oldName in names:
            names.remove(oldName)
            print(oldName + "已删除!")
        else:
            print(oldName + "不存在！")
    else:
        names.append(user)

row = input("请输入座位行数：")
column = input("请输入座位列数：")
print("---------- 讲台 ----------")
if int(row) * int(column) >= len(names):
    count = 0
    while True:
        index = random.randint(0, len(names) - 1)
        name = names.pop(index)
        print(name + "　" * (10 - len(name)), end="")
        count += 1
        if count % int(column) == 0:
            print()
        if len(names) == 0:
            break
else:
    print("座位不够")
