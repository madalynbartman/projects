from turtle import *
from theme import set_theme
import random

def grow(length, decrease, angle, noise=0):

    if length > 10:
        
        width = (length / 10)
        forward(length)

        new_length = length * decrease
        if noise > 0:
            new_length *= random.uniform(0.9,1.1)

        angle_l = angle + random.gauss(0, noise)
        angle_r = angle + random.gauss(0, noise)

        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        right(angle_r)     

        backward(length)   

set_theme()

penup()
goto(0,-400)
pendown()
left(90)

grow(150, 0.8, 20, 10)

tracer(True)
exitonclick()