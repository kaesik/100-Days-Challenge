from CoffeeMachine_variables import *


def show_menu():
    """Shows menu with products and costs"""
    print("MENU:")
    for key, value in MENU.items():
        name = key.title()
        cost = list(value.items())[1][1]
        print(f"{name}: ${cost}")
    print("")


def show_resources():
    """Shows the remaining resources"""
    print("RESOURCES:")
    print(f"{water[0].title()}: {water[1]}ml")
    print(f"{milk[0].title()}: {milk[1]}ml")
    print(f"{coffee[0].title()}: {coffee[1]}g")


def prompt():
    """Console where you can write what to do"""
    print(f"What would you like? (espresso/latte/cappuccino)")
    console = input()
    return console


def off():
    """"Turn off the machine"""
    return print("─────────────────────\n─────MACHINE OFF─────\n─────────────────────")


def insert_coin():
    """Insert coin and write the summary"""
    while True:
        q = input("How many quarters?: ")
        try:
            q = int(q)
            break
        except ValueError:
            print("Incorrect. Write a number.")
    print(f"Inserted ${round(q * 0.25, 2)}")
    while True:
        d = input("How many dimes?: ")
        try:
            d = int(d)
            break
        except ValueError:
            print("Incorrect. Write a number.")
    print(f"Inserted ${round(q * 0.25 + d * 0.10, 2)}")
    while True:
        n = input("How many nickles?: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("Incorrect. Write a number.")
    print(f"Inserted ${round(q * 0.25 + d * 0.10 + n * 0.05, 2)}")
    while True:
        p = input("How many pennies?: ")
        try:
            p = int(p)
            break
        except ValueError:
            print("Incorrect. Write a number.")
    print(f"Inserted ${round(q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01, 2)}")
    return round(q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01, 2)


def check_money(money_insert, money_needed):
    """Checks if inserted is enough money to buy coffee"""
    if money_insert >= money_needed:
        return True
    else:
        return False


def check_resources(check_coffee):
    """Checks if there is enough resources to do coffee"""
    if water[1] >= MENU[check_coffee]["ingredients"]["water"] and \
        milk[1] >= MENU[check_coffee]["ingredients"]["milk"] and \
            coffee[1] >= MENU[check_coffee]["ingredients"]["coffee"]:
        return True
    else:
        return False


def refill():
    """Replenish the resources"""
    water[1] = 300
    milk[1] = 300
    coffee[1] = 100
    print("RESOURCES REPLENISHED\n")
