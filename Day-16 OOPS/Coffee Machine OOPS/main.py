from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_item = Menu()

is_machine_on = True

while is_machine_on:
    choice = input(f"What would you like to have? ({menu_item.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_machine_on = False
    else :
        drink = menu_item.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
