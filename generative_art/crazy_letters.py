from turtle import *
from theme import set_theme
import random

set_theme(canvas_width = 1200,
          canvas_height=800,
          thickness=3)

size = 80
n = 1
for y in range(300, -300, -size):

    prime = random.random()

    for x in range(-500+size, 500, size):

        # set color
        r = random.random() * prime
        g = random.random() * prime
        b = random.random() * prime
        pencolor(r,g,b)

        # original point
        px = x + random.uniform(size/4, size/4)
        py = y + random.uniform(size/4, size/4)

        # set start point to original point
        px_start = px
        py_start = py

        # move to starting point 
        penup()
        goto(px_start,py_start)
        pendown()

        # draw the shape 
        for i in range(n):

            # random end point
            px_end = x + random.uniform(-size/4, size/4)
            py_end = y + random.uniform(-size/4, size/4)

            # draw connexting line
            goto(px_end, py_end)

            # reset starting point 
            px_start = px_end
            py_start = py_end

        # go back to orignal point
        goto(px,py)

    # increase n
    n += 1
        

tracer(True)
exitonclick()