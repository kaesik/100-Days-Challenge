import arts
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(arts.logo)
working_program = True


def caesar(caesar_text, caesar_shift, caesar_direction):
    caesar_shift = caesar_shift % len(alphabet)
    end_text = ""
    for letter in caesar_text:
        if letter not in alphabet:
            end_text += letter
            continue
        old_index = alphabet.index(letter)
        if caesar_direction == "encode":
            new_index = old_index + caesar_shift
        elif caesar_direction == "decode":
            new_index = old_index - caesar_shift
        if new_index > (len(alphabet) - 1):
            new_index -= len(alphabet)
        end_text += alphabet[new_index]
    print(f"The {caesar_direction}d text is '{end_text}'")


while working_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(caesar_text=text, caesar_shift=shift, caesar_direction=direction)
    continuing = input("Type 'yes' if you want to go again. Otherwise press enter:\n")
    if continuing == "yes":
        continue
    else:
        working_program = False
        print("Goodbye")
