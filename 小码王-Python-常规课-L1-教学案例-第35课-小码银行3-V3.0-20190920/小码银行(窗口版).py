import tkinter  # 导入tkinter模块
import tkinter.messagebox  # 导入tkinter.messagebox模块

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
        tkinter.messagebox.showinfo("余额", "您的账户余额为：" + str(self.balance))

    # 存钱
    def save(self, money):
        self.balance += money
        self.operation = "存入" + str(money)
        tkinter.messagebox.showinfo("提示", "存入成功")

    # 取钱
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            self.operation = "取出" + str(money)
            tkinter.messagebox.showinfo("提示", "取出成功")
        else:
            tkinter.messagebox.showwarning("警告", "没钱还想来得瑟")

    # 记录
    def record(self):
        f = open(self.name + ".txt", "a")
        text = self.name + "," + self.password + "," + str(self.balance) + "," + self.operation + "\n"
        f.write(text)
        f.close()


window = tkinter.Tk()  # 创建窗口
window.geometry("400x500")  # 设置窗口大小
window.title("注册/登录")  # 设置窗口标题

# 创建文字标签
label1 = tkinter.Label(window, text="小码银行", font=("微软雅黑", 20))
# 粘贴文字
label1.pack(pady=50)

label2 = tkinter.Label(window, text="账户名", font=("微软雅黑", 20))
label2.pack(pady=0)

# 创建“账户名”输入框
entry1 = tkinter.Entry(window, font=("微软雅黑", 20))
entry1.pack()

# “密码”文字标签
label3 = tkinter.Label(window, text="密码", font=("微软雅黑", 20))
label3.pack(pady=0)

# “密码”输入框
entry2 = tkinter.Entry(window, font=("微软雅黑", 20))
entry2.pack()

# 注册函数
def signin():
    name = entry1.get()  # 获取账户名
    pw = entry2.get()  # 获取密码
    try:
        open(name + ".txt", "r")
    except:
        # 创建账户和生成txt文件
        user = Account(name, pw, 0, "创建账户")
        user.record()
        tkinter.messagebox.showinfo("提示", "注册成功")
    else:
        # 提示账户已存在，请重新输入
        tkinter.messagebox.showwarning("警告", "账户已存在，请重新输入")

# 登录函数
def login():
    name = entry1.get()  # 获取账户名
    pw = entry2.get()  # 获取密码
    try:
        f1 = open(name + ".txt", "r")
    except:
        tkinter.messagebox.showinfo("提示", "账户不存在，请先注册")
    else:
        # 读取密码
        lines = f1.readlines()
        line = lines[len(lines) - 1]
        lineList = line.split(",")
        password1 = lineList[1]

        # 密码正确
        if pw == password1:
            balance1 = int(lineList[2])
            user = Account(name, pw, balance1, "登录账户")
            user.record()
            tkinter.messagebox.showinfo("提示", "登录成功")

            # 销毁 注册/登录窗口
            window.destroy()
            # 功能页窗口
            homepage = tkinter.Tk()
            homepage.geometry("400x500")
            homepage.title("功能页")
            label11 = tkinter.Label(homepage, text="小码银行", font=("微软雅黑", 20))
            label11.pack(pady=50)
            # 输入框
            label22 = tkinter.Label(homepage, text="请输入存取金额", font=("微软雅黑", 20))
            label22.pack()
            entry11 = tkinter.Entry(homepage, font=("微软雅黑", 20))
            entry11.pack(pady=10)

            # 查询余额
            def checkMoney():
                user.check()

            # 存钱
            def saveMoney():
                money = int(entry11.get())
                user.save(money)
                user.record()

            # 取钱
            def withdrawMoney():
                money = int(entry11.get())
                user.withdraw(money)
                user.record()
            
            # 查询余额按钮
            btn11 = tkinter.Button(homepage, text="查询余额", font=("微软雅黑", 20), width=20, command=checkMoney)
            btn11.pack(pady=10)
            # 存钱按钮
            btn22 = tkinter.Button(homepage, text="存钱", font=("微软雅黑", 20), width=20, command=saveMoney)
            btn22.pack(pady=10)
            # 取钱按钮
            btn33 = tkinter.Button(homepage, text="取钱", font=("微软雅黑", 20), width=20, command=withdrawMoney)
            btn33.pack(pady=10)

        # 密码错误
        else:
            tkinter.messagebox.showerror("错误", "密码错误")

# “登录”按钮
btn1 = tkinter.Button(window, text="登录", font=("微软雅黑", 20), width=20, command=login)
btn1.pack(pady=20)

# “注册”按钮
btn2 = tkinter.Button(window, text="注册", font=("微软雅黑", 20), width=20, command=signin)
btn2.pack()


























