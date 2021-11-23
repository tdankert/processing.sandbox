from p5 import *

'''
Definitions of some system variables.
'''
global height
global width

global dim


def setup():
    size(1366, 768)
    no_stroke()

    no_loop()


def draw():
    background(8)
    for x in range(2000):
        cx = random_gaussian(30, 600)
        cy = random_uniform(0, height)
        draw_ellipse(cx, cy)
    save()


# def key_pressed(event):
#     background(104)


def draw_ellipse(x, y):
    fill(random_gaussian(127, 64), random_uniform(127), random_uniform(51), 127)

    ellipse_width = random_uniform(low=10, high=80)
    ellipse_height = random_uniform(low=10, high=80)
    rotate(random_uniform(0, 45))
    ellipse(x, y, ellipse_width, ellipse_height)


def draw_gradient(x, y):
    radius = dim / 2
    h = random_uniform(0, 360)
    for r in range(radius, 0, -1):
        fill(h, 90, 90)
        ellipse(x, y, r, r)
        h = (h + 1) % 360


run()
