import turtle


t = turtle
t.bgcolor("black")
t.pencolor("white")
t.fillcolor("white")
t.shape("turtle")


# draw eq trianle
def draw_eq():
    t.begin_fill()
    for i in range(3):
        t.right(120)
        t.forward(100)
    t.end_fill()

# eq tri spiral
for i in range(4):
    draw_eq()
    t.right(90)


t.exitonclick()