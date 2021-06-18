import turtle
import time
import random

# 创建小海龟t1
t1 = turtle.Turtle()
t1.pensize(3)
t1.shape("turtle")
t1.speed(0)

# 绘制小人
# 头
t1.circle(30)
# 右眼
t1.penup()
t1.goto(10, 30)
t1.left(90)
t1.pendown()
t1.forward(10)
# 左眼
t1.penup()
t1.goto(-10, 30)
t1.pendown()
t1.forward(10)

# 身体和腿
t1.penup()
t1.goto(0, 0)
t1.pendown()
t1.left(180)
t1.forward(80)
t1.right(45)
t1.forward(60)
t1.backward(60)
t1.left(135)
t1.forward(60)
t1.right(90)
t1.forward(40)
# 手
t1.penup()
t1.goto(0, -20)
t1.pendown()
t1.left(90)
t1.forward(60)
t1.left(45)
t1.forward(10)
# 另一只手
t1.penup()
t1.goto(0, -30)
t1.pendown()
t1.right(45)
t1.forward(60)
t1.right(45)
t1.forward(10)

# 显示文字
t1.penup()
t1.goto(80, 30)
t1.pendown()
t1.write("送你小心心~~~", font=("微软雅黑", 15))

t2 = turtle.Turtle()
turtle.tracer(False)  # 取消小海龟画图过程
t2.hideturtle()
numList = [100]  # 存放所有爱心的x坐标
colorList = ["red", "yellow", "blue", "pink", "orange", "grey",
             "silver", "purple", "black"]
while True:
    if numList[0] > 100 and numList[0] % 100 == 0:
        numList.append(100)
    if numList[0] > 500:
        numList.pop(0)
    # 清除屏幕
    t2.clear()
    for i in numList:
        # 设置随机颜色
        colorIdx = random.randint(0, len(colorList) - 1)
        t2.color(colorList[colorIdx])
        
        a = random.randint(-10, 10)
        # 画爱心
        # 左半个爱心
        t2.penup()
        t2.goto(i, -10 + a)
        t2.begin_fill() # 开始填充
        t2.pendown()
        t2.setheading(90)
        t2.circle(10 , 180)
        t2.circle(30, 70)
        # 右半个爱心
        t2.penup()
        t2.goto(i, -10 + a)
        t2.pendown()
        t2.setheading(90)
        t2.circle(-10 , 180)
        t2.circle(-30, 70)
        t2.end_fill() # 结束填充
        # 爱心右移
        idx = numList.index(i)
        numList[idx] += 10

    turtle.update() # 将小海龟画的图刷新出来
    time.sleep(0.1) # 让程序等待一会
    
    
