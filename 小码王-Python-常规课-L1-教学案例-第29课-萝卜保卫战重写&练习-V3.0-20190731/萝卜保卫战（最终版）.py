import turtle
import time
import random

turtle.bgpic("bg.gif")
turtle.setup(800, 600)

# 创建小海龟t
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
##t.goto(10, 10)
# 创建兔子rabbit
turtle.register_shape("rabbit.gif")  # 注册兔子形状
rabbit = turtle.Turtle()
rabbit.shape("rabbit.gif")
rabbit.penup()
rabbit.goto(100, 100)
# 创建胡萝卜carrot
turtle.register_shape("carrot.gif")
carrot = turtle.Turtle()
carrot.shape("carrot.gif")
carrot.penup()
carrot.goto(100, 200)
# 显示得分word
word = turtle.Turtle()
word.penup()
word.goto(-350, 250)
word.hideturtle()
word.write("得分：0", font=("微软雅黑", 15))

score = 0
# 判断收集胡萝卜和计算分数
def collect():
    global score
    dis1 = t.distance(carrot)
    if dis1 < 10:
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        carrot.goto(x, y)
        score = score + 1
        word.clear()
        word.write("得分：" + str(score)  , font=("微软雅黑", 15))  
        if score >= 3:
            turtle.bgpic("win.gif")
            turtle.update()

def checkBound():
    x = t.xcor()
    y = t.ycor()
    if x < -400 or x > 400 or y < -300 or y > 300:
        t.undo()

def setSpeed():
    global tSpeed
    tx = t.xcor()
    if tx > -100 and tx < 100:
        tSpeed = 10
    else:
        tSpeed = 1

# 小海龟前进
def ahead():
    t.penup()
    setSpeed()
    t.forward(tSpeed)
    checkBound()
    collect()
        
# 小海龟后退
def back():
    t.penup()
    setSpeed()
    t.backward(tSpeed)
    checkBound()
    collect()

    
# 小海龟左转
def turnLeft():
    t.left(30)


# 小海龟右转
def turnRight():
    t.right(30)

    
# 兔子朝着小海龟移动
def rabbitRun():
    angle = rabbit.towards(t)
    rabbit.setheading(angle)
    rx = rabbit.xcor()
    if rx > -100 and rx < 100:
        rSpeed = 1
    else:
        rSpeed = 10
    rabbit.forward(rSpeed)
        
turtle.listen()  # 开始监测事件
turtle.onkeypress(ahead, "Up")  # 监测 上键 按下事件
turtle.onkeypress(back, "Down") # 监测 下键 按下事件
turtle.onkeypress(turnLeft, "Left")  # 监测 左键 按下事件
turtle.onkeypress(turnRight, "Right")  # 监测 右键 按下事件

while True:
    rabbitRun()
    rx = rabbit.xcor()
    ry = rabbit.ycor()
    tx = t.xcor()
    ty = t.ycor()
    dis = rabbit.distance(t)
    if dis < 10:
        turtle.bgpic("lose.gif")
        turtle.update()
        break
    if score >= 3:
        break

rabbit.hideturtle()
t.hideturtle()
carrot.hideturtle()

time.sleep(2)
turtle.bye()











