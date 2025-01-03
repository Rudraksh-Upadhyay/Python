from turtle import Turtle, Screen

t = Turtle()
# t.forward(100)
# t.penup()
# t.goto(200, 0)
# t.pendown()
# t.forward(100)

for _ in range(10):
    t.forward(10)
    t.penup()
    t.goto(t.xcor()+10, 0)
    t.pendown()

# print(t.position())

MyScreen = Screen()
MyScreen.exitonclick()