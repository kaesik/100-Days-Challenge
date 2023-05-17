import tkinter as tk
import pandas as pd
import random as rd
import time as tm

# ------- CONSTANTS ------- #
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
FONT = ("Ariel", 12, "normal")
TIME = 3


# ------- VARIABLES ------- #
title = "Title"
word = "Word"


card_front = "./images/card_front.png"
card_back = "./images/card_back.png"

known_words = []

# --------- DATA ---------- #
data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict()
lang_1 = list(data_dict.keys())[0]
lang_2 = list(data_dict.keys())[1]
dict_1 = [value for value in data_dict[lang_1].values()]
dict_2 = [value for value in data_dict[lang_2].values()]


# --------- TIMER --------- #
def timer():
    global index, word_1, word_2
    index, word_1, word_2 = random_word()
    start(word_1)
    count_down(TIME, word_2)


def start(text):
    card_img.config(file=card_front)
    card.itemconfig(word_text, text=text)
    card.itemconfig(title_text, text=lang_1)


def count_down(count, text):
    if count > 0:
        window.after(1000, count_down, count - 1, text)
    else:
        card_img.config(file=card_back)
        card.itemconfig(word_text, text=text)
        card.itemconfig(title_text, text=lang_2)


def random_word():
    index_ = rd.randint(0, (len(dict_1) - 1))
    word_1_ = dict_1[index_]
    word_2_ = dict_2[index_]
    return index_, word_1_, word_2_


def delete_word(word_1, word_2):
    dict_1.remove(word_1)
    dict_2.remove(word_2)
    known_words.append(word_1)
    counter.itemconfig(counter_text, text=str(len(known_words)))


# ------- FUNCTIONS ------- #
def x_command():
    try:
        timer()
    except ValueError:
        card.itemconfig(title_text, text="Congratulation")
        card.itemconfig(word_text, text="That's all.")


def y_command():
    try:
        delete_word(word_1, word_2)
        timer()
    except ValueError:
        card.itemconfig(title_text, text="Congratulation")
        card.itemconfig(word_text, text="That's all.")


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
title_text = card.create_text(400, 150, text=title, font=TITLE_FONT)
word_text = card.create_text(400, 263, text=word, font=WORD_FONT)

counter = tk.Canvas(width=200, height=132, bg=BACKGROUND_COLOR, highlightthickness=0)
counter.create_image(100, 66, image=counter_img)
counter.grid(column=1, row=1)
counter.create_text(100, 110, text="KNOWN WORDS", font=FONT)
counter_text = counter.create_text(100, 50, text=str(len(known_words)), font=WORD_FONT)


# BUTTONS
x_img = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_img, highlightthickness=0, command=x_command)
x_button.grid(column=0, row=1)

y_img = tk.PhotoImage(file="./images/right.png")
y_button = tk.Button(image=y_img, highlightthickness=0, command=y_command)
y_button.grid(column=2, row=1)


index, word_1, word_2 = random_word()
start(word_1)
count_down(TIME, word_2)


window.mainloop()
