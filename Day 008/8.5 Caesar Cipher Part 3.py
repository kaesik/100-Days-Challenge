alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(caesar_text, caesar_shift, caesar_direction):
    end_text = ""
    for letter in caesar_text:
        old_index = alphabet.index(letter)
        if caesar_direction == "encode":
            new_index = old_index + caesar_shift
        elif caesar_direction == "decode":
            new_index = old_index - caesar_shift
        if new_index > (len(alphabet) - 1):
            new_index -= len(alphabet)
        end_text += alphabet[new_index]
    print(f"The {caesar_direction}d text is {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(caesar_text=text, caesar_shift=shift, caesar_direction=direction)