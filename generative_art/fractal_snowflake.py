from turtle import *

shape("turtle")
speed(0)

def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def create_snowflake(sides, length):
    colors = ["green", "blue", "yellow", "orange"]
    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)
    
# goto(x, y) will move the turtle to another 
# position and you can draw another snowflake 
# at a different location on the canvas

create_snowflake(4, 200)

mainloop()
