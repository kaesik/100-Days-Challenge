#TODO-1: Import and print the logo from art.py when the program starts.✔️
import CaesarCipher_arts
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(CaesarCipher_arts.logo)
working_program = True

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?✔
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).

#TODO-3: What happens if the user enters a number/symbol/space?✔
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
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

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
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



