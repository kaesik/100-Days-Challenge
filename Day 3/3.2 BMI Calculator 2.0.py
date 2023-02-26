height = input("Enter your height here [m]: ")
weight = input("Enter your weight here [kg]: ")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

bmi = round(float(weight) / float(height) ** 2, 1)

if bmi <= 18.5:
    print(f"You'r BMI is {bmi}, you're underweight.")
elif 18.5 < bmi <= 25:
    print(f"You'r BMI is {bmi}, you have a normal weight.")
elif 25 < bmi <= 30:
    print(f"You'r BMI is {bmi}, you're overweight.")
elif 30 < bmi <= 35:
    print(f"You'r BMI is {bmi}, you're obese.")
else:
    print(f"You'r BMI is {bmi}, you're clinically obese.")