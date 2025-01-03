from turtle import Turtle, Screen, colormode
import random
import colorgram

t = Turtle()
t.width(10)
t.speed(0)
colormode(255)

#Get colors from the image->

colors = colorgram.extract('hirst_image.jpeg', 25)
color_list = []
for i in range(len(colors)):
    color_list.append(tuple(colors[i].rgb))
print(color_list)

color_second_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205),
                     (109, 67, 85), (39, 35, 34), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48),
                     (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108),
                     (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59)]

a = 50
for _ in range(5):

    for _ in range(5):
        # t.circle(10)
        t.pencolor(random.choice(color_second_list))

        # t.begin_fill()
        for _ in range(4):
            t.forward(1)
            t.right(90)
        # t.end_fill()

        t.fillcolor("red")
        t.up()
        t.goto(t.xcor()+50, t.ycor())
        t.down()
    t.up()
    t.goto(0, t.ycor()+a)
    t.down()


my_screen = Screen()
my_screen.exitonclick()
my_screen.title("HIRST_PAINTING")
