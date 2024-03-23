import pygame
import random

# global variables
width = 600
height = 400
n = 50

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
def draw_bars(array, screen):
    screen.fill(pygame.Color("black"))
    n = len(array)
    for i in range(n):
        draw_bar(array, i, screen, pygame.Color("orange"))

# initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((width,height))

# animation loop
animating = True
while animating:

    # create array
    array = random.sample(range(1,n+1), n)

    # drawing the array
    draw_bars(array, screen)

    # update
    pygame.display.flip()

    # pause
    pygame.time.wait(1)

    # track user interaction
    for event in pygame.event.get():

        # user the pygame window to end animation
        if event.type == pygame.QUIT:
            animating = False