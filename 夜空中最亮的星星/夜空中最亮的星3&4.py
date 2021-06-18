import turtle
import random
import time

turtle.bgpic("背景.png")
turtle.setup(800, 600)
turtle.tracer(False)

t1 = turtle.Turtle()

def star5(x, y):
    size = random.randint(10, 30)
    # 画五角星
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color("white")
    t1.begin_fill() 
    for i in range(5):
        t1.forward(size)
        t1.right(144)
    t1.end_fill()
    turtle.update()

def star4(x, y):
    size = random.randint(10, 30)
    # 画四角星
    # t1 = turtle.Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color("white")
    t1.begin_fill() 
    for i in range(4):
        t1.left(75)
        t1.forward(size)
        t1.right(165)
        t1.forward(size)
    t1.end_fill()
    turtle.update()

xList = []
yList = []
def selectStar(x, y):
    xList.append(x)
    yList.append(y)
    num = random.randint(0, 1)
    if num == 0:
        star5(x, y)
    else:
        star4(x, y)

def test():
    while True:
        t1.clear()
        # 星星闪动
        for i in range(len(xList)):
            x = xList[i]
            y = yList[i]
            num = random.randint(0, 1)
            if num == 0:
                star5(x, y)
            else:
                star4(x, y)
        time.sleep(0.3)
        

turtle.listen()  # 开始监测事件
turtle.onscreenclick(selectStar)  # 监测鼠标点击事件
turtle.onkeypress(test, "space")  # 监测按键按下事件
