#Write your code below this row 👇
summary = 0
for number in range(1, 101):
    if number % 2 == 0:
        summary += number
print(summary)