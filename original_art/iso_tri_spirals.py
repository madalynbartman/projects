import turtle


t = turtle
t.bgcolor("black")
t.pencolor("white")
t.fillcolor("white")
t.shape("turtle")

# draw isosceles tri
def draw_iso():
    t.begin_fill()
    t.right(60)
    t.forward(100)
    t.right(150)
    t.forward(100)
    t.right(150)
    t.forward(100)
    t.end_fill()

# iso tri spiral
for i in range(5):
    draw_iso()
    t.right(90)

t.exitonclick()
