#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

#input_word = "DBCA"
input_word = input("Enter a word: ").upper()
phonetic_word = [nato_alphabet[letter] for letter in input_word]
print(phonetic_word)
