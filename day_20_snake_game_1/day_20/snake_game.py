import time
from turtle import Screen
from snake import Snake, GameOver
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

#CREATE SNAKE
snake = Snake()

#CREATE FOOD
food = Food()
scoreboard = ScoreBoard()

game_is_on = True

def off_game():
    game_is_on = False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# x = 0
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# turtles = []
# for position in starting_position:
#     t = Turtle()
#     t.up()
#     t.shape("square")
#     t.color("white")
#     t.goto(position)
#     turtles.append(t)


# SNAKE MOVEMENT


while game_is_on:
    # scoreboard = ScoreBoard()
    screen.update()

    time.sleep(0.1)
    # for turtle in turtles:
    #     turtle.forward(20)

    # for tur_num in range(len(Snake.turtles)-1, 0, -1):
    #     new_x = Snake.turtles[tur_num-1].xcor()
    #     new_y = Snake.turtles[tur_num-1].ycor()
    #     Snake.turtles[tur_num].goto(new_x, new_y)
    #
    # Snake.turtles[0].forward(20)
    snake.move()

    #FOOD DETECTION/COALITION
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.create_new()
        scoreboard.update_score()

    #COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        GameOver()
        game_is_on = False


    #COLLISION WITH TAIL
    for turtle in snake.turtles[1:len(snake.turtles)]:
        if snake.head.distance(turtle) < 10:
            GameOver()
            game_is_on = False


screen.exitonclick()