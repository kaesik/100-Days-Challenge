import SecretAuctionProgram_arts
import os

biders = []


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def add_new_bider(name, bid):
    biders.append({
        "name": name,
        "bid": bid,
        })


def fun_highest_bidder(biders_list):
    highest_bid = 0
    winner_name = ""
    for value in biders_list:
        if highest_bid < int(value["bid"]):
            highest_bid = int(value["bid"])
    for person in biders_list:
        if highest_bid == int(person["bid"]):
            winner_name = person["name"]
    return highest_bid, winner_name


def working_program():
    program_working = True
    while program_working:
        add_new_bider(
            input("What is your name?: "),
            int(input("What is your bid?: $"))
        )
        continuing = input("Are there any other bidders? Type 'yes' or press enter.\n").lower()
        clear()
        if continuing != "yes":
            program_working = False


print(SecretAuctionProgram_arts.logo)
working_program()
highest_bid = fun_highest_bidder(biders)[0]
winner_name = fun_highest_bidder(biders)[1]
print(f"The winner is {winner_name} with a bid of ${highest_bid}")