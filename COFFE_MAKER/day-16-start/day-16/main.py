# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.circle(50)
# timmy.forward(100)
# # print(timmy)
#
# my_screen = Screen()
# my_screen.bgcolor("lightgreen")
# my_screen.title("KASHISH UPADHYAY")
# # my_screen.getshapes()
# # my_screen.canvheight
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable(["POKEMON", "TYPE"])
table.add_row(["PIKACHU", "ELECTRIC"])
table.add_row(["CHARMANDER", "FIRE"])
table.add_row(["SQUIRTLE", "WATER"])

table.align = "r"
print(table.align)
print(table)

