from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items().split("/")
    a = 1
    print("\nITEMS AVAILABLE:\n")
    for i in range(len(options)-1):
        print(f"{a}:{options[i]}")
        a += 1

    choice = input("\nWhat would you like to order?")

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        # print(drink)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)