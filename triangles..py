from p5 import *


def setup():
    size(1366, 768)
    no_stroke()

    no_loop()


def draw():
    background(9)
    fill(random_gaussian(127, 64), random_uniform(127), random_uniform(51), 127)
    triangle(100, 100, 1000, 500, 300, 70)


run()