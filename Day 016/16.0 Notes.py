# from turtle import *
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrange1")
# timmy.forward(100)
#
# my_sreen = Screen()
# print(my_sreen.canvheight)
#
# my_sreen.exitonclick()

from prettytable import *

table = PrettyTable()

table.add_column("Pokemon Name",
                 ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type",
                 ["Electric", "Fire", "Water"])
table.align = "l"

print(table)