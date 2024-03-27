import turtle
import random

# Hexagon
# for i in range(5):
#     turtle.forward(150)
#     turtle.right(60)

for i in range(100):
    # set a random color
    turtle.color(random.random(), random.random(), random.random())
    # move random units forward
    turtle.forward(random.randrange(25,76))
    # move random direction
    angle = random.randrange(0,181)
    if random.random() > 0.5:
        # turn left
        turtle.left(angle)
    else:
        # turn right
        turtle.right(angle)
        
turtle.mainloop()
