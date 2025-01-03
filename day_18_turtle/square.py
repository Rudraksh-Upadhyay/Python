from turtle import Turtle,Screen

MyTurtle = Turtle()

# MyTurtle.forward(100)
# MyTurtle.left(90)
# MyTurtle.forward(100)
# MyTurtle.left(90)
# MyTurtle.forward(100)
# MyTurtle.left(90)
# MyTurtle.forward(100)
for _ in range(4):
    MyTurtle.forward(100)
    MyTurtle.left(90)


MyScreen = Screen()
MyScreen.bgcolor("lightblue")
MyScreen.exitonclick()