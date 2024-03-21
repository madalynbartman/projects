from turtle import *
import random

setup(1000, 1000)

def tiling(x,y,s,l, mode="straight"):

    # we've reached the final level of recursion & now draw 
    if l == 0:

        if mode == "straight":

            if random.random() < 0.5:

                # vertical line
                penup()
                goto(x, y-s)
                pendown()
                goto(x,y+s)

            else:

                # horizonatl line
                penup()
                goto(x-s, y)
                pendown()
                goto(x+s, y)

        elif mode == "diagonal":

            if random.random() < 0.5:
                # top left to bottom right
                penup()
                goto(x-s, y+s)
                pendown()
                goto(x+s,y-s)

            else:
                # bottom left to top right
                penup()
                goto(x-s, y-s)
                pendown()
                goto(x+s, y+s)


    # split screen and go to next level of recursion
    else:
        s /= 2
        l -= 1
        tiling(x-s,y+s,s,l,mode)
        tiling(x+s,y+s,s,l,mode)
        tiling(x-s,y-s,s,l,mode)
        tiling(x+s,y-s,s,l,mode)

width(3)
hideturtle()
tracer(False)
tiling(0,0,400,5,mode="diagonal")
tracer(True)
exitonclick()