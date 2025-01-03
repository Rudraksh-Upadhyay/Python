from turtle import Turtle,Screen

timmy_the_turtle = Turtle()

#APPEARANCE
timmy_the_turtle.shape("turtle")

#COLOUR CONTROL
timmy_the_turtle.color("magenta")


#MOVEMENT
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

#screen
screen = Screen()
screen.exitonclick()
# screen.bgcolor("black")