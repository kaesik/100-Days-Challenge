# LIST COMPREHENSION
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Kamil"
letter_list = [letter for letter in name]
print(letter_list)

range_list = [n*2 for n in range(1, 5)]
print(range_list)

names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleonore", "Freddie"]
short_names = [name for name in names_list if len(name) < 5]
print(short_names)
capitalized_names = [name.upper() for name in names_list if len(name) > 5]
print(capitalized_names)