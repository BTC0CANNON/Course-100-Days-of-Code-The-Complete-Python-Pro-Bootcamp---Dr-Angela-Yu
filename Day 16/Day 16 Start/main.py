# from turtle import Turtle
# 
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkGoldenrod3")
# timmy.forward(100)
# 
# print(timmy)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
