import turtle, random

turtle.speed(10000)

def draw(n):
    if n >= 3:

        for i in range(1,n+1):
            turtle.forward(30)
            turtle.left(180-((n-2)*180/n))
        n -= 1
        draw(n)

turtle.right(90)
turtle.penup()
turtle.forward(250)
turtle.left(90)
turtle.pendown()
draw(50)

#태양 그리기

#  from turtle import *
#  def star(x):
#      if x <= 1:
#          return
#      else:
#          fd(200)
#          left(170)
#          star(x-1)


#  color('red','yellow')
#  begin_fill()
#   star(37)
#  end_fill()

#스카이라인 그리기
# xpos=-200
# ypos=-200
# blocksize=50

# def block(x,y):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()

#     color=random.random()
#     turtle.fillcolor(color,color,color)
#     turtle.begin_fill()

#     for i in range(4):
#         turtle.forward(50)
#         turtle.right(90)
#     turtle.end_fill()


# for building in range(5):
#     h=random.randint(1,10)
#     for story in range(h):
#         block(xpos,ypos)
#         ypos += blocksize

#     ypos = -200
#     xpos += blocksize
# turtle.hideturtle()


#다각형 꽃 그리기

#  def f(n):
#      for i in range(1,n+1):
#          for j in range(1, n+1):
#              turtle.pensize(2)
#              turtle.fd(50)
#              turtle.rt(180-((n-2)*180/n))
#          turtle.left(180-((n-2)*180/n))

#  f(24)

# t = turtle.Turtle()

# 나무 그리기

# def tree(t,branchlen):
#     if branchlen > 5:
#         t.forward(branchlen)
#         t.right(30)
#         tree(t,branchlen-15)
#         t.left(60)
#         tree(t,branchlen-15)
#         t.right(30)
#         t.backward(branchlen)


# def main():
#     t=turtle.Turtle()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     tree(t,75)

# main()



# 스파이럴 그리기

#  def draw_spiral(t, lineLen):
#      if lineLen > 0:
#          t.forward(lineLen)
#          t.right(90)
#          draw_spiral(t, lineLen - 5)

#  draw_spiral(turtle, 100)

# 막대 그래프 그리기

# def draw_bar(t, height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write("  " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)

# t = turtle.Turtle()
# t.color("blue", "skyblue")
# t.pensize(3)

# x1 = random.randint(1, 200)
# x2 = random.randint(1, 200)
# x3 = random.randint(1, 200)
# x4 = random.randint(1, 200)
# x5 = random.randint(1, 200)
# x6 = random.randint(1, 200)
# x7 = random.randint(1, 200)

# xlist = [x1, x2, x3, x4, x5, x6, x7]

# for i in xlist:
#     draw_bar(t, i)

input('Press RETURN to exit')
