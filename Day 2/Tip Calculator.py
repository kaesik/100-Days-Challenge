print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
calculate = round(((bill*tip/100)+bill)/people, 2)
print(f"Each person should pay: ${calculate}")