from turtle import Turtle, Screen
import random

t = Turtle()

# #Square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
#
# #Pentagon
# for _ in range(5):
#     t.color("red")
#     t.forward(100)
#     t.right(72)
#
# #Hexagon
# for _ in range(6):
#     t.color("green")
#     t.forward(100)
#     t.right(60)
#
# #Heptagon
# for _ in range(7):
#     t.color("orange")
#     t.forward(100)
#     t.right(51.42857142857143)
#
# #Octagon
# for _ in range(8):
#     t.color("brown")
#     t.forward(100)
#     t.right(45)
#
# #Nonagon
# for _ in range(9):
#     t.color("purple")
#     t.forward(100)
#     t.right(40.52380952380952)
#
# #Decagon
# for _ in range(10):
#     t.color("blue")
#     t.forward(100)
#     t.right(36)

colours = ['red', 'purple', 'orange', 'brown', 'green', 'black', 'blue', 'dark slate blue']

for i in range(4,11):
    angle = 360/i
    t.color(random.choice(colours))
    for _ in range(i):

        t.forward(100)
        t.right(angle)

#Screen
MyScreen = Screen()
MyScreen.exitonclick()