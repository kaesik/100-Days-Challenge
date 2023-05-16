import tkinter as tk
import pandas as pd
import random as rd

# ------- CONSTANTS ------- #
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
FONT = ("Ariel", 12, "normal")
TIME = 3


# ------- VARIABLES ------- #
card_front = "./images/card_front.png"
card_back = "./images/card_back.png"

# --------- DATA ---------- #
data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict()
lang_1 = list(data_dict.keys())[0]
lang_2 = list(data_dict.keys())[1]
dict_1 = [value for value in data_dict[lang_1].values()]
dict_2 = [value for value in data_dict[lang_2].values()]


# --------- TIMER --------- #
def count_down(count, text):
    if count > 0:
        window.after(1000, count_down, count - 1, text)
    else:
        card_img.config(file=card_back)
        card.itemconfig(word_text, text=text)
        card.itemconfig(title_text, text=lang_2)


def random_word():
    index = rd.randint(0, (len(data) - 1))
    word_1 = dict_1[index]
    word_2 = dict_2[index]
    return index, word_1, word_2


def delete_word(index):
    dict_1.pop(index)
    dict_2.pop(index)


# ------- FUNCTIONS ------- #
def x_command():
    index, word_1, word_2 = random_word()
    card_img.config(file=card_front)
    card.itemconfig(word_text, text=word_1)
    card.itemconfig(title_text, text=lang_1)
    count_down(TIME, word_2)


def y_command():
    index, word_1, word_2 = random_word()
    card_img.config(file=card_front)
    card.itemconfig(word_text, text=word_1)
    card.itemconfig(title_text, text=lang_1)
    count_down(TIME, word_2)


# ---------- UI ----------- #
window = tk.Tk()
window.title("Flash Card 📇")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# IMAGES
card_img = tk.PhotoImage(file=card_front)
counter_img = tk.PhotoImage(file="./images/counter.png")


# CANVAS
card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.create_image(400, 263, image=card_img)
card.grid(column=0, row=0, columnspan=3)
title_text = card.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = card.create_text(400, 263, text="Word", font=WORD_FONT)

counter = tk.Canvas(width=200, height=132, bg=BACKGROUND_COLOR, highlightthickness=0)
counter.create_image(100, 66, image=counter_img)
counter.grid(column=1, row=1)
counter.create_text(100, 110, text="KNOWN WORDS", font=FONT)
counter_text = counter.create_text(100, 50, text="0", font=WORD_FONT)


# BUTTONS
x_img = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_img, highlightthickness=0, command=x_command)
x_button.grid(column=0, row=1)

y_img = tk.PhotoImage(file="./images/right.png")
y_button = tk.Button(image=y_img, highlightthickness=0, command=y_command)
y_button.grid(column=2, row=1)


x_command()
window.mainloop()
