import random
import words, arts

chosen_word = random.choice(words.word_list)
lives = 6

display = []
print(arts.logo)
for letter in chosen_word:
    display.extend("_")
while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"The letter '{guess}' has been already guessed. Try another one.")
    i = -1
    for letter in chosen_word:
        i += 1
        if guess == letter:
            display[i] = guess
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the chosen word.")
        lives -= 1
        print(arts.stages[lives])
        if lives == 0:
            break
    print(f"{' '.join(display)}")

if "_" not in display:
    print("You win!")
else:
    print(f"You lose! The chosen word is {chosen_word}")
