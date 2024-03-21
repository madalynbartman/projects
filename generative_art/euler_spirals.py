from turtle import *
from theme import set_theme
import random

def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step

# cool pattern 1
# set_theme(tracer_value = 1, hide_turtle = False)
# euler_curve(step_size = 40, angle_step = 1.00, n_steps = 600)

# cool pattern 2
# set_theme(tracer_value = 100)
# euler_curve(step_size = 2, angle_step = 1.01, n_steps = 100000)  

# cool pattern 3
set_theme(tracer_value = 100)
euler_curve(step_size = 3, angle_step = 1.99, n_steps = 100000)

tracer(True)
exitonclick()