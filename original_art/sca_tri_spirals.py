import turtle


t = turtle
t.bgcolor("black")
t.pencolor("white")
t.fillcolor("white")
t.shape("turtle")

# draw scalene tri
def draw_sca():
    t.begin_fill()
    t.right(60)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.end_fill()

# sca tri spiral
for i in range(5):
    draw_sca()
    t.right(90)

t.exitonclick()
