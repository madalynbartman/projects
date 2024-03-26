import pygame
import pygame.gfxdraw

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255) # 255 = max = white. These represent red, green, blue values
black = (0, 0, 0) # 0 = min = black

running = True
while running:
    screen.fill(black) # fills our screen with black

    for i in range(screen_width):
        pygame.gfxdraw.pixel(screen, i, screen_height // 2, white)

    for i in range(screen_height):
        pygame.gfxdraw.pixel(screen, screen_width // 2, i, white)

    for i in range(screen_height):
        pygame.gfxdraw.pixel(screen, i, i, white)

    for i in range(screen_width):
        pygame.gfxdraw.pixel(screen, i, screen_height - i, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Added for the challenge exercise

    for i in range(screen_width):
        pygame.gfxdraw.pixel(screen, i, screen_height // 4, white)

    for i in range(screen_height):
        pygame.gfxdraw.pixel(screen, screen_width // 4, i, white)   

    pygame.display.flip()
