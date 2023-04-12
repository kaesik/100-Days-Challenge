height = input("Enter your height here [m]: ")
weight = input("Enter your weight here [kg]: ")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

bmi = int(float(weight) / float(height) ** 2)
print(bmi)