from turtle import Turtle, Screen
import random

angle = [90, 180, 270, 360]
colours = ['firebrick', 'saddle brown', 'blue violet', 'dark green']

def randomAngle():
    return random.choice(angle)

def randomColour():
    return random.choice(colours)

t = Turtle()
t.pensize(10)
t.speed(0)

def path(angle):
    c = randomColour()
    t.color(c)
    t.right(angle)
    t.forward(50)
    angle1 = randomAngle()
    path(angle1)

path(randomAngle())

MyScreen = Screen()
MyScreen.exitonclick()


# for _ in range(200):
#     t.color(random.choice(colours))
#     t.forward(10)
#     t.setheading(randomAngle())