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

# DICT COMPREHENSION
import random
names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleonore", "Freddie"]
students_scores = {name:random.randint(1, 100) for name in names_list}
print(students_scores)

passed_students = {name:"passed" for (name, score) in students_scores.items() if score > 50}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# LOOPING THROUGH DICTIONARIES
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# LOOP THROUGH A DATA FRAME
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# LOOP THROUGH ROWS OF A DATA FRAME
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.score)