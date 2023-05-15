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
title_text = "title"
word_text = "word"

card_front = "./images/card_front.png"
card_back = "./images/card_back.png"

known_words = []
counter_text = str(len(known_words))
timer = None


# --------- DATA ---------- #
data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict()
lang_1 = list(data_dict.keys())[0]
lang_2 = list(data_dict.keys())[1]
dict_1 = (value for key, value in data_dict[lang_1][1])
dict_2 = [word for word in data_dict[lang_2][1]]


# --------- TIMER --------- #
def count_down(count):
    global timer
    card_img.config(file=card_front)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        card_img.config(file=card_back)


def random_word():
    index = rd.randint(0, (len(data)-1))
    word_1 = data_dict[lang_1][index]
    word_2 = data_dict[lang_2][index]
    print(index, lang_1, lang_2)


# ------- FUNCTIONS ------- #
def x_command():
    print(dict_1)


def y_command():
    count_down(TIME)


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
card.create_text(400, 150, text=title_text, font=TITLE_FONT)
card.create_text(400, 263, text=word_text, font=WORD_FONT)

counter = tk.Canvas(width=200, height=132, bg=BACKGROUND_COLOR, highlightthickness=0)
counter.create_image(100, 66, image=counter_img)
counter.grid(column=1, row=1)
counter.create_text(100, 110, text="KNOWN WORDS", font=FONT)
counter.create_text(100, 50, text=counter_text, font=WORD_FONT)


# BUTTONS
x_img = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_img, highlightthickness=0, command=x_command)
x_button.grid(column=0, row=1)

y_img = tk.PhotoImage(file="./images/right.png")
y_button = tk.Button(image=y_img, highlightthickness=0, command=y_command)
y_button.grid(column=2, row=1)


window.mainloop()
