from turtle import *
from theme import set_theme
import random

set_theme(canvas_width = 600, thickness = 2)

size = 50
noise = 0.0
for y in range(400, -400, -size):
    for x in range(-250, 250, size):

        # move to the location
        penup()
        goto(x,y)
        pendown()

        # rotate
        angle = random.uniform(-noise, noise)
        right(angle)

        # draw square
        for i in range(4):
            forward(size)
            right(90)

        # rotate back
        left(angle)

    # add noise
    noise += 4.0

tracer(True)
exitonclick()