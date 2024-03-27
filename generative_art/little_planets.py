w, h = 800, 800

pfc = (255, 255, 255)
olc = (0, 0, 0)
bgc = (255, 255, 255)

pw = 6
rw = 6

def draw_planet(position, ps):
    translate(position[0], position[1])
    starting_height = random(ps/4, ps/2)
    starting_width = random(ps*1.2, ps*2)

    rotate(random(2*PI))

    # Add background
    fill(pfc[0], pfc[1], pfc[2])
    stroke_weight(pw)
    circle(0, 0, ps)

    # Add rings
    no_fill()
    stroke_weight(rw)
    for i in range(int(random(3, 9))):
        ellipse(0, 0, starting_height + i * 10, starting_width + i * 30)

    # Cover rings
    stroke_weight(pw)
    fill(pfc[0], pfc[1], pfc[2])
    arc(0, 0, ps, ps, 1.5*PI, 2.5*PI)

def setup():
    size(w, h)
    frame_rate(1)

    pixel_density(2)

def draw():
    background(bgc[0], bgc[1], bgc[2])
    draw_planet((w//2, h//2), 200)
