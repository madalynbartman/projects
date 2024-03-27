import turtle
# First original art
# Replicartion of Pete's steam profile photo

t = turtle
t.bgcolor("light green")
t.penup()
t.pensize(50)

def draw_left_eye():
    t.goto(-90, 200)
    t.right(90)
    t.pendown()
    t.forward(100)
    t.penup()

def draw_right_eye():
    t.goto(0,200)
    t.pendown()
    t.forward(100)
    t.penup()

def draw_mouth():
    t.goto(-135,0)
    t.pendown()
    t.left(100)
    t.forward(200)

draw_left_eye()
draw_right_eye()
draw_mouth()

turtle.exitonclick()