from functions import *

water = list(list(resources.items())[0])
milk = list(list(resources.items())[1])
coffee = list(list(resources.items())[2])
money = 0

while True:
    show_menu()
    console = prompt().lower()
    if console == "info":
        print("report - to get report about resources\n"
              "off - to turn off the machine\n"
              "menu - to print menu\n"
              "refill - replenishes resources\n")
    elif console == "report":
        show_resources()
        print(f"Money: ${money}\n")
        continue
    elif console == "off":
        off()
        break
    elif console == "menu":
        show_menu()
        continue
    elif console == "refill":
        refill()
        continue
    elif console == "espresso" or console == "latte" or console == "cappuccino":
        if check_resources(console):
            coin = round(insert_coin(), 2)
            if check_money(coin, MENU[console]["cost"]):
                change = coin - MENU[console]["cost"]
                water[1] -= MENU[console]["ingredients"]["water"]
                milk[1] -= MENU[console]["ingredients"]["milk"]
                coffee[1] -= MENU[console]["ingredients"]["coffee"]
                money += MENU[console]["cost"]
                coin = 0
                print(f"Here is ${round(change, 2)} change.")
                print(f"Here is your {console.title()}, enjoy!")
            elif not check_money(coin, MENU[console]["cost"]):
                print("Not enough money inserted! Money refunded.")
                coin = 0
                continue
        elif water[1] < MENU[console]["ingredients"]["water"]:
            print("Not enough water! Refill needed.")
            continue
        elif milk[1] < MENU[console]["ingredients"]["milk"]:
            print("Not enough milk! Refill needed.")
            continue
        elif coffee[1] < MENU[console]["ingredients"]["coffee"]:
            print("Not enough coffee! Refill needed.")
            continue
    else:
        print("Incorrect decision. Write 'info'.\n")
        continue
