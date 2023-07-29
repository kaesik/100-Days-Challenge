import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    word = input("Enter a word: ").upper()
    try:
        if len(word) == 0:
            raise ValueError
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("error: please use letters")
        generate()
    except ValueError:
        print("error: cannot be blank")
        generate()
    else:
        print(output_list)

generate()
