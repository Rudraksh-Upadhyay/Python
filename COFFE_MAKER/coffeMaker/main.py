MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 80,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
status = True


def is_resource_available(saman):
    for items in saman:
        if resources[items] < saman[items]:
            print(f"{items} is not available in the machine")
            return False
    return True


def process_coin(item):
    print("...MAKE PAYMENT...")
    print(f"Amount to be paid = {item['cost']}")
    print("Please insert coin")
    total = 0
    total += int(input("How many 10 Rupees:")) * 10
    total += int(input("How many 20 Rupees:")) * 20
    total += int(input("How many 50 Rupees:")) * 50
    print(f"Total amount paid = {total}")
    return total


while status:
    choice = input("What would you like to have? (espresso/latte/cappuccino):")

    if choice == "off":
        print("Turning off the machine.")
        status = False
        break

    if choice == "report":
        print("Machine Have ->")
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: "
              f"${profit} \n")

    else:
        drink = MENU[choice]
        ingredients = drink["ingredients"]
        if is_resource_available(ingredients):
            payment = process_coin(drink)
            if payment >= drink["cost"]:
                change = payment - drink["cost"]
                print(f"Thank you for your order...Here is your change {change}")

                resources["water"] -= ingredients["water"]
                resources["milk"] -= ingredients["milk"]
                resources["coffee"] -= ingredients["coffee"]
                profit += drink["cost"]
                print(f"Here is your order {choice}...Please Enjoy")
            else:
                print("INSUFFICIENT AMOUNT")
        else:
            print("Not enough resources to make this drink")