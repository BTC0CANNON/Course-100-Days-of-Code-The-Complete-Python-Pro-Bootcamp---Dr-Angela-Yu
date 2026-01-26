from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_on = True
while machine_on:
    options = menu.get_items()
    menu_choice = input(f"What would you like? ({options}): ")

    if menu_choice == 'off':
        print("The machine will now turn off.")
        machine_on = False
        quit()
    elif menu_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(menu_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
