# from turtle import Turtle, Screen
#
# og = Turtle()
# print(og)
#
# og.shape("turtle")
# og.color("coral")
# og.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
print(table.align)
table.align = "l"
print(table)
print(table.align)
