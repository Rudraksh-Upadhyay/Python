from turtle import Turtle, Screen, colormode
import random

t = Turtle()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

# for _ in range(500):
#     t.color(random_color())
#     t.speed(9)
#     t.width(10)
#     t.forward(10)
#     t.left(random.randint(0,360))
for i in range(3,11):
    angle = 360/i
    t.color(random_color())
    for _ in range(i):

        t.forward(100)
        t.right(angle)

MyScreen = Screen()
MyScreen.exitonclick()
