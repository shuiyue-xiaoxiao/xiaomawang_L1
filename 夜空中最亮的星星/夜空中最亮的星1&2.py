import turtle

turtle.bgpic("背景.png")
turtle.setup(800, 600)
turtle.tracer(False)

def star5(x, y):
    # 画五角星
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color("white")
    t1.begin_fill() 
    for i in range(5):
        t1.forward(30)
        t1.right(144)
    t1.end_fill()
    turtle.update()

def star4(x, y):
    # 画四角星
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color("white")
    t1.begin_fill() 
    for i in range(4):
        t1.left(75)
        t1.forward(30)
        t1.right(165)
        t1.forward(30)
    t1.end_fill()
    turtle.update()

turtle.listen()  # 开始监测事件
turtle.onscreenclick(star4)  # 监测鼠标点击事件
