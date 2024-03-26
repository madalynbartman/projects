import threading
import random
import time
import turtle

# Define a list of colors
COLORS = ['red', 'orange', 'gold', 'green', 'blue', 'purple']


# Define a function for drawing a shape with a random color and size
def draw_shape():
    # Create a turtle object
    t = turtle.Turtle()

    # Set the pen color and size to random values
    t.pencolor(random.choice(COLORS))
    t.pensize(random.randint(1, 10))

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw a random shape with a random size and color
    shape = random.choice(['circle', 'square', 'triangle'])
    size = random.randint(10, 100)
    if shape == 'circle':
        t.circle(size)
    elif shape == 'square':
        for i in range(4):
            t.forward(size)
            t.right(90)
    elif shape == 'triangle':
        for i in range(3):
            t.forward(size)
            t.left(120)

    # Hide the turtle
            t.hideturtle()

# Define a function for creating threads that draw shapes
def draw_thread():
    while True:
        # Draw a shape 
        draw_shape()

        # Sleep for a random amount of time
        time.sleep(0.3)

# Create a canvas for drawing on
canvas = turtle.Screen()

# Create 10 threads for drawing shapes
for i in range(10):
    t = threading.Thread(target=draw_thread)
    t.start()

# Start the turtle event loop
    turtle.mainloop()
    