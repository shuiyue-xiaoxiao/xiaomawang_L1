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

# 查询余额按钮
btn11 = tkinter.Button(homepage, text="查询余额", font=("微软雅黑", 20), width=20)
btn11.pack(pady=10)
# 存钱按钮
btn22 = tkinter.Button(homepage, text="存钱", font=("微软雅黑", 20), width=20)
btn22.pack(pady=10)
# 取钱按钮
btn33 = tkinter.Button(homepage, text="取钱", font=("微软雅黑", 20), width=20)
btn33.pack(pady=10)
