from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()