import pygame
import pygame.gfxdraw
import random

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255) # 255 = max = white. These represent red, green, blue values
black = (0, 0, 0) # 0 = min = black

random_colors = [(123, 30, 22), (33, 60, 223), (220, 120, 55)]

running = True

def draw_flat_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x + i, y, color)

def draw_vertical_line(screen, x, y, height, color):
    for i in range(height):
        pygame.gfxdraw.pixel(screen, x, y + i, color)

def draw_plus_sign(screen, x, y, size, color):
    draw_flat_line(screen, x - (size // 2), y, size, color)
    draw_vertical_line(screen, x, y - (size // 2), size, color)

plusX = screen_width // 2
plusY = screen_height // 2

this_length = 15

cursor_list = [] # [(50, 50), (75, 75)] every unit (in parenthesis) is separated by a comma

while running:
    screen.fill(black) # fills our screen with black
    
    draw_plus_sign(screen, plusX, plusY, this_length, random.choice(random_colors))

    key = pygame.key.get_pressed()

    for plus_sign in cursor_list:
        draw_plus_sign(screen, plus_sign[0], plus_sign[1], this_length, white)

    if key[pygame.K_SPACE]:
        new_place = [plusX, plusY]
        cursor_list.append(new_place)

    if key[pygame.K_UP]:
        # plusY == 1
        plusY = plusY - 1
    elif key[pygame.K_DOWN]:
        # plusY += 1
        plusY = plusY + 1
    if key[pygame.K_LEFT]:
        plusX = plusX - 1
    elif key[pygame.K_RIGHT]:
        plusX = plusX + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    pygame.display.flip()
