import turtle

turtle.shape("turtle")

# 调整小海龟初始位置
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()

# 房子主体
turtle.fillcolor("navy")
turtle.begin_fill()
for i in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

# 房子的门
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(120)
turtle.end_fill()

# 门把手
turtle.backward(60)
turtle.right(90)
turtle.forward(5)
turtle.dot(10, "black")

# 移动到画窗户的位置
turtle.penup()
turtle.right(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(60)
turtle.pendown()

# 透明的窗户
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(4):
    turtle.forward(60)
    turtle.right(90)
turtle.end_fill()

# 移动到屋顶的右下角
turtle.penup()
turtle.forward(80)
turtle.right(90)
turtle.forward(100)
turtle.pendown()

# 画屋顶
turtle.fillcolor("coral")
turtle.begin_fill()
for i in range(3):
    turtle.left(120)
    turtle.forward(240)
turtle.end_fill()

















