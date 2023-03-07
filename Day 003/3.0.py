height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride the Rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif 45 <= age <= 55:
        bill = 0
        print(f"Midlife crisis tickets are free")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3
else:
    print("You can't ride the Rollercoaster")

print(f"Your total bill for the ticket is ${bill}")
