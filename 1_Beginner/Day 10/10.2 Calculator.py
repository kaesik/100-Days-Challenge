from Calculator_functions import *
from Calculator_arts import *



print(logo)
num_1 = float(input("What is the first number: "))
for key in operations:
    print(key)
operating_symbol = input("Pick an operation from the line above: ")
num_2 = float(input("What is the second number: "))

while True:
    answer = calculation(num_1, num_2, operating_symbol)
    print(f"{num_1} {operating_symbol} {num_2} = {answer}")
    continuing = input(f"Type 'y' to continue calculating with {answer}, or press enter to exit.\n")
    if continuing != "y":
        print("Leaving the program.")
        break
    num_1 = answer
    operating_symbol = input("Pick another operation: ")
    num_2 = float(input("What is the next number: "))