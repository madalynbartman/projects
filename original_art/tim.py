import turtle
from turtle import Screen, Turtle

# drawing tim's background

t = turtle
t.bgcolor("red")
t.fillcolor("black")
screen = Screen()
screen.setup(450, 450)
t.shape("turtle")
t.speed(0)

def checkers():
    # box 1
    t.penup()
    t.goto(-230,225)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    t.end_fill()
    
    # box 2
    t.penup()
    t.forward(300)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    t.end_fill()


    # box 4 (middle)
    t.penup()
    t.goto (-80,75)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    t.end_fill()


    # box 5
    t.penup()
    t.goto(-230, -67) 
    t.pendown()
    t.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    t.end_fill()

    # box 6
    t.penup()
    t.forward(300)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    t.end_fill()   
  

checkers()

t.exitonclick()
