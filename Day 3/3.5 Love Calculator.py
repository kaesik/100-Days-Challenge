# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

count_t = name1_lower.count("t")+name2_lower.count("t")
count_r = name1_lower.count("r")+name2_lower.count("r")
count_u = name1_lower.count("u")+name2_lower.count("u")
count_e = name1_lower.count("e")+name2_lower.count("e")
count_l = name1_lower.count("l")+name2_lower.count("l")
count_o = name1_lower.count("o")+name2_lower.count("o")
count_v = name1_lower.count("v")+name2_lower.count("v")

love_score_str = str(count_t + count_r + count_u + count_e) + str(count_l + count_o + count_v + count_e)
love_score = int(love_score_str)

print('')
print(f'T occurs {count_t} times')
print(f'R occurs {count_r} times')
print(f'U occurs {count_u} times')
print(f'E occurs {count_e} times')
print('')
print(f'L occurs {count_l} times')
print(f'O occurs {count_o} times')
print(f'V occurs {count_v} times')
print(f'E occurs {count_e} times')
print('')

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
