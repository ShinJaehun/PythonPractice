import turtle

turtle.setup(width = 500, height = 500)
t = turtle.Pen()
t.color("yellow")
ts = t.getscreen()
ts.bgcolor("black")#배경색
t.right(60)
t.begin_fill()
for i in range(1,4):#가운데 지붕
    t.forward(60)
    t.right(120)
t.end_fill()
t.color("brown")
t.begin_fill()
t.up()
t.forward(60)
t.right(30)
t.down()
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.forward(100)
t.right(90)
t.forward(60)

t.end_fill()
t.right(90)
t.forward(90)
t.left(90)
t.forward(130)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.color("yellow")
t.begin_fill()
for i in range(1,4):#오른쪽 지붕
    t.left(120)
    t.forward(50)
t.end_fill()
t.color("brown")

t.right(90)
t.forward(120)
t.right(90)
t.forward(420)
t.right(90)
t.forward(120)
t.right(90)

t.color("yellow")
t.begin_fill()
for i in range(1,4):#왼쪽 지붕
    t.forward(50)
    t.left(120)
t.end_fill()
t.forward(50)
t.color('brown')
t.right(90)
t.forward(50)
t.left(90)
t.forward(130)
t.begin_fill()#성벽 채우기
t.forward(60)
t.forward(130)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(120)
t.right(90)
t.forward(420)
t.right(90)
t.forward(120)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(130)

t.end_fill()
t.color("green")
t.up()
t.right(90)
t.forward(70)
t.left(90)
t.forward(30)
t.down()
t.begin_fill()#땅 채우기
t.forward(250)
t.left(180)
t.forward(500)
t.left(90)
t.forward(90)
t.left(90)
t.forward(500)
t.left(90)
t.forward(90)
t.left(90)
t.forward(250)
t.end_fill()
t.right(90)
t.up()
t.forward(300)
t.color("white")
t.right(90)
t.forward(30)
t.down()
t.begin_fill()#달 만들기
t.circle(60)
t.end_fill()
t.up()
t.left(20)      #별들 만들기
t.forward(200)
t.begin_fill()
t.circle(10)
t.end_fill()
t.left(160)
t.forward(100)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(110)
t.forward(70)
t.begin_fill()
t.circle(10)
t.end_fill()
t.left(100)
t.forward(150)
t.begin_fill()
t.circle(10)
t.end_fill()
t.left(60)
t.forward(150)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(90)
t.forward(150)
t.begin_fill()
t.circle(10)
t.end_fill()
t.left(150)
t.forward(130)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(230)
t.forward(100)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(110)
t.forward(300)
t.begin_fill()
t.circle(10)
t.end_fill()
t.left(160)
t.forward(100)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(110)
t.forward(70)
t.begin_fill()
t.circle(10)
t.end_fill()
t.forward(90)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(170)
t.forward(270)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(30)
t.forward(60)
t.begin_fill()
t.circle(10)
t.end_fill()
t.forward(80)
t.begin_fill()
t.circle(10)
t.end_fill()
t.right(170)
t.forward(130)
t.begin_fill()
t.circle(10)
t.end_fill()
t.forward(270)
t.begin_fill()
t.circle(10)
t.end_fill()
input('Press RETURN to exit')
