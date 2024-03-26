import turtle

# chose your own shape
running = True # creating a var called true

while running:
    print('enter triangle, square, or exit:')
    entered = input()

    if entered == 'triangle':
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    elif entered == 'square':
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif entered == 'exit':
        running = False
        print('exiting..')
    # extras from the chapter challenges
    elif entered == 'pentagon':
        for i in range(5):
            turtle.forward(100)
            turtle.right(72)
    elif entered == 'hexagon':
        for i in range(6):
            turtle.forward(100)
            turtle.right(60)
    else:
        print('not a command')
