# Fractal: A curve or geometric figure, each part of which has the same
# similar patterns recur at progressively smaller scales.
# tech with tim fractal art

from turtle import *

shape("turtle")
speed(0)

def tree(size, levels, angle):
    # need base case for recursive function to tell it when to stop calling itself
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return
    
    forward(size) # we draw our branch after aligning the turtle and angling it correcctly
    right(angle)

    tree(size * 0.8, levels -1, angle)

    left(angle * 2)

    tree(size * 0.8, levels -1, angle)

    right(angle)
    backward(size)

left(90)
tree(70, 7, 30)

mainloop() # makes it so the turtle screen doesn't close immediately. have to press x to close.

