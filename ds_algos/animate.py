import pygame
import random

# global variables
width = 600
height = 400
n = 50

# dictonary for colors
COLORS = {
    "background": (35,35,40),
    "regular": (255,248,240),
    "highlight1": (239,71,111),
    "highlight2": (255,209,102),
    "highlight3": (17,138,178),
    "sorted": (6,214,160)
}

# function to draw a single abr
def draw_bar(array, i, screen, color):
    n = len(array)
    w, h = screen.get_size()
    bar_width = w // n
    bar_height = h // n * array[i]
    x = bar_width * i
    y = h - bar_height
    bar = pygame.Rect(x, y, bar_width, bar_height)
    pygame.draw.rect(screen, color, bar)

# function to visualize an entire array using a bar chart
def draw_bars(array, screen, highlight1 = [], highlight2 = [], highlight3 = [], sorted = False):
    screen.fill(COLORS["background"])
    n = len(array)
    if sorted:
        for i in range(n):
            draw_bar(array, i, screen, COLORS["sorted"])
    else: 
        for i in range(n):
            draw_bar(array, i, screen, COLORS["regular"])
        for i in highlight1:
            draw_bar(array, i, screen, COLORS["highlight1"])
        for i in highlight2:
            draw_bar(array, i, screen, COLORS["highlight2"])
        for i in highlight3:
            draw_bar(array, i, screen, COLORS["highlight3"])

# create array and sorting process generator
array = random.sample(range(1,n+1), n)
from bubble_sort import bubble_sort
process = bubble_sort(array)

# initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((width,height))

# animation loop
animating = True
while animating:

    # next step in the sorting process
    array, highlight1, highlight2, highlight3 = next(process, (None, None, None, None))

    # bar chart visulaization 
    if array is not None:
        draw_bars(array, screen, highlight1, highlight2, highlight3)
    else: 
        array = list(range(1, n+1))
        draw_bars(array, screen, sorted=True)

    # update
    pygame.display.flip()

    # pause
    pygame.time.wait(10)

    # track user interaction
    for event in pygame.event.get():

        # user the pygame window to end animation
        if event.type == pygame.QUIT:
            animating = False
