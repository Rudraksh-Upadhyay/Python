from turtle import Turtle, Screen
import random

race_start = False
screen = Screen()
screen.title("TURTLE RACE")
screen.setup(500, 400)
number_of_users = screen.numinput("NUMBER OF BETTERS", "Enter the number of users/betters")
bet_list = []
user_input_list = []
color_list = ["red", "green", "purple", "blue", "brown"]


def color():
    color = []
    for i in range(int(number_of_users)):
        color.append(color_list[i])
    return color


for i in range(int(number_of_users)):
    bet = screen.numinput("Bet amount", f"User {i+1} Enter bet amount")
    bet_list.append(bet)
for i in range(int(number_of_users)):
    user_input = screen.textinput("TURTLE RACE", f"User {i+1} CHOOSE THE TURTLE WHICH WILL WIN THE RACE"
                                                 f"\nEnter the choice ({color()})->")
    user_input_list.append(user_input)

for i in range(int(number_of_users)):
    print(f"turtle choice of user {i+1} is {user_input_list[i]}")



total_bet_amount = 0

for i in range((len(bet_list))):
    total_bet_amount += bet_list[i]

turtle_list = []


def starting_ending_line():
    tim = Turtle()
    tim.hideturtle()
    tim.speed(9)
    tim.color("black")
    tim.penup()
    tim.goto(-210, -200)
    tim.pendown()
    tim.left(90)
    tim.forward(400)
    tim.penup()
    tim.goto(210, -200)
    tim.pendown()
    # t.left(90)
    tim.forward(400)
    # t.write("START LINE", align="center", font=("Courier", 24, "normal"))


def back_to_begin():
    y = -80
    for i in range(0, int(number_of_users)):
        t = Turtle(shape="turtle")
        t.color(color_list[i])
        t.penup()
        t.goto(-230, y)
        y += 40
        turtle_list.append(t)


def off_screen():
    screen.bye()


if user_input_list:
    race_start = True
    back_to_begin()
    starting_ending_line()

while race_start:

    for t in turtle_list:
        speed = random.randint(0, 10)
        t.forward(speed)
        if t.xcor() > 210:
            race_start = False
            winner_color = t.color()[0]
            print(f"{winner_color} turtle wins!!!")
            for i in range(int(number_of_users)):
                if user_input_list[i] == winner_color:
                    print(f"User {i+1} wins {total_bet_amount}")
                else:
                    print("LOST MONEY")

    # print("want rematch??")
# choice = screen.textinput("REMATCH??", "Yes or No")
# if choice.lower() == "yes":
#     back_to_begin()
#     race_start = True
#     starting_ending_line()
# else:
#     off_screen()

screen.exitonclick()
