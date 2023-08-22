# # from turtle import Turtle, Screen


# # timmy = Turtle()
# # timmy.shape("turtle")
# # timmy.color("DarkMagenta")
# # timmy.forward(100)
# # myscreen = Screen()
# # print(myscreen.canvheight)
# # myscreen.exitonclic

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon name", ["Pikachu", "Squirtle"])
# table.add_column("Pokemon type", ["Electric", "Water"])
# table.align = "c"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on= True








while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        mm.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            