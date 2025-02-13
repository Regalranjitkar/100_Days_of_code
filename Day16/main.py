from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:

    choice = input(f"Choose a drink {menu.get_items()} : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice) is not None:
        chosen_item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(chosen_item):
            if money_machine.make_payment(chosen_item.cost):
                coffee_maker.make_coffee(chosen_item)