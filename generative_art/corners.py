import pygame
import pygame.gfxdraw
import random

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255) # 255 = max = white. These represent red, green, blue values
black = (0, 0, 0) # 0 = min = black
red = (255, 0, 0)
blue = (0,0,255)

running = True

def draw_flat_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x + i, y, color)

def draw_vertical_line(screen, x, y, height, color):
    for i in range(height):
        pygame.gfxdraw.pixel(screen, x, y + i, color)

while running:
    screen.fill(black) # fills our screen with black

    for i in range(100):
        thisX, thisY = (random.randrange(0, screen_width), random.randrange(0, screen_height))
        this_length = random.randrange(0, 200)

        draw_flat_line(screen, thisX, thisY, this_length, white)
        draw_vertical_line(screen, thisX, thisY, this_length, white)

    # draw_vertical_line(screen, screen_width // 2, screen_height // 2, 100, blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    pygame.display.flip()
