# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
number = 0
avarage = 0
for height in student_heights:
    avarage += height
    number += 1
avarage = int(avarage/number)

print(avarage)