from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20

class Snake:


    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            t = Turtle()
            t.up()
            t.shape("square")
            t.color("white")
            t.goto(position)
            self.turtles.append(t)


    def move(self):
        for tur_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[tur_num - 1].xcor()
            new_y = self.turtles[tur_num - 1].ycor()
            self.turtles[tur_num].goto(new_x, new_y)

        self.turtles[0].forward(MOVEMENT)


    def create_new(self):
        t_new = Turtle()
        t_new.up()
        t_new.shape("square")
        t_new.color("white")
        t_new.goto(self.turtles[-1].xcor(), self.turtles[-1].ycor())
        self.move()
        self.turtles.append(t_new)

    def reset(self):
        for i in self.turtles:
            i.goto(1000, 1000)
        self.turtles = []
        self.__init__()


    def up(self):
        heading = self.turtles[0].heading()
        if heading == 0:
            self.turtles[0].setheading(90)

        if heading == 180:
            self.turtles[0].setheading(90)

    def down(self):

        heading = self.turtles[0].heading()
        if heading == 0:
            self.turtles[0].setheading(270)

        if heading == 180:
            self.turtles[0].setheading(270)

    def left(self):
        heading = self.turtles[0].heading()
        if heading == 90:
            self.turtles[0].setheading(180)
        if heading == 270:
            self.turtles[0].setheading(180)

    def right(self):
        heading = self.turtles[0].heading()
        if heading == 90:
            self.turtles[0].setheading(0)
        if heading == 270:
            self.turtles[0].setheading(0)



class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("red")
        self.write("GAME OVER", False, "center", ("Arial", 24, "normal"))


