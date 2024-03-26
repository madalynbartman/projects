import turtle
turtle.down()

for side in range(24):
    print(side)
    turtle.forward(100 + side)
    turtle.right(90 + side) # this side var is sick

input()