from turtle import Turtle, colormode, Screen
import random

t = Turtle()
colormode(255)
t.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, b, g)
    return tup


for _ in range(60):
    t.pencolor(random_color())
    t.circle(100)
    t.left(6)

my_screen = Screen()
my_screen.exitonclick()