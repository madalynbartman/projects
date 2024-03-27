import pygame
import pygame.gfxdraw
import random
import math

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

    key = pygame.key.get_pressed()

    for i, plus_sign in enumerate(cursor_list):
        # make rainbows by changing the offset (sin) or the colors (channels)
        # essentially make rainbows by fading colors
        # ri = math.sin(i * .04) * 77 + 178 # 50 is the lowest value
        rr = math.sin(i * 0.4) * 77 + 178 # red
        rg = math.sin(i * 0.4 + 15) * 77 + 178 # green
        rb = math.sin(i * 0.4 + 10) * 77 + 178 # blue

        # set brightness
        fader = (math.sin(i * .03) + 1) / 2
        rr = rr * fader
        rg = rg * fader
        rb = rb * fader

        # add a sizer to set length of cursor
        sizer = int(math.sin(i * 0.033) * 35 + 37)
        draw_plus_sign(screen, plus_sign[0], plus_sign[1], sizer, 
                       (rr, rg, rb))
    
    # draw cursor
    draw_plus_sign(screen, plusX, plusY, this_length, random.choice(random_colors))

    # First we take top left quarter of screen, make a copy
    cropped = pygame.Surface((screen_width // 2, screen_height // 2))
    cropped.blit(screen, (0,0), pygame.Rect(0, 0, screen_width // 2, screen_height // 2))

    # flip that copy on just the y axis, paste below
    below_flipped = pygame.transform.flip(cropped, False, True)
    screen.blit(below_flipped, pygame.Rect(0,screen_height // 2, screen_width // 2, screen_height))

    # flip original copy on just x axis, paste to the right
    top_right = pygame.transform.flip(cropped, True, False)
    screen.blit(top_right, pygame.Rect(screen_width // 2, 0, screen_width, screen_height // 2))

    # finally flip both axis, paste bottom right
    bottom_right = pygame.transform.flip(cropped, True, True)
    screen.blit(bottom_right, pygame.Rect(screen_width // 2, screen_height // 2, screen_width, screen_height))

    if key[pygame.K_SPACE]:
        new_place = [plusX, plusY]
        cursor_list.append(new_place)

    if key[pygame.K_UP]:
        # plusY == 1
        plusY = plusY - 2
    elif key[pygame.K_DOWN]:
        # plusY += 1
        plusY = plusY + 2
    if key[pygame.K_LEFT]:
        plusX = plusX - 2
    elif key[pygame.K_RIGHT]:
        plusX = plusX + 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    pygame.display.flip()
