# 账户类
class Account():
    def __init__(self, name, password, balance, operation):
        self.name = name
        self.password = password
        self.balance = balance
        self.operation = operation
        print(self.name, "账户" + self.operation + "成功")

    # 查询余额
    def check(self):
        print("当前余额：", self.balance)

    # 存钱
    def save(self, money):
        self.balance += money
        self.operation = "存入" + str(money)

    # 取钱
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            self.operation = "取出" + str(money)
        else:
            print("没钱还想来得瑟")

    # 记录
    def record(self):
        f = open(self.name + ".txt", "a")
        text = self.name + "," + self.password + "," + str(self.balance) + "," + self.operation + "\n"
        f.write(text)
        f.close()

# 输入信息
name = input("请输入账户名称：")
password = input("请输入账户密码：")
try:
    file = open(name + ".txt", "r")
# 账户不存在
except:
    balance = int(input("请输入账户余额："))
    operation = "创建账户"
# 账户存在
else:
    # 读取txt文件中的记录
    lines = file.readlines()
    line = lines[len(lines) - 1]
    lineList = line.split(",")
    balance = int(lineList[2])
    operation = "登录账户"

# 创建账户
user = Account(name, password, balance, operation)
user.record()

while True:
    num = input("""
1、查询余额
2、存钱
3、取钱
""")
    if num == "1":
        user.check()
    elif num == "2":
        money = int(input("请输入想存的钱："))
        user.save(money)
        user.record()
    elif num == "3":
        money = int(input("请输入想取的钱："))
        user.withdraw(money)
        user.record()
    else:
        print("兄dei，输入123啊")






