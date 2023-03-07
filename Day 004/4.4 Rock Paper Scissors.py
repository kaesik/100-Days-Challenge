import random

your_choice = int(input("What do you choose? Typ 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if your_choice == 0:
    if computer_choice == 0:
        print("You choose Rock,\nComputer also choose Rock.\nDraw! ")
    elif computer_choice == 1:
        print("You choose Rock,\nComputer choose Paper.\nYou lose! ")
    elif computer_choice == 2:
        print("You choose Rock,\nComputer choose Scissors.\nYou win! ")
elif your_choice == 1:
    if computer_choice == 0:
        print("You choose Paper,\nComputer choose Rock.\nYou win! ")
    elif computer_choice == 1:
        print("You choose Paper,\nComputer also choose Paper.\nDraw! ")
    elif computer_choice == 2:
        print("You choose Paper,\nComputer choose Scissors.\nYou lose! ")
elif your_choice == 2:
    if computer_choice == 0:
        print("You choose Scissors,\nComputer choose Rock.\nYou lose! ")
    elif computer_choice == 1:
        print("You choose Scissors,\nComputer choose Paper.\nYou win! ")
    elif computer_choice == 2:
        print("You choose Scissors,\nComputer also choose Scissors.\nDraw! ")