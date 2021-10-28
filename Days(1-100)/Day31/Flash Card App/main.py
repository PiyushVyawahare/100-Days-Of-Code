import random
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/M-E.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# -------------------------------------- UI DESIGN -------------------------------------- #


def flip_card():
    canvas.itemconfig(card_title, text="Marathi", fill="white")
    canvas.itemconfig(card_word, text=current_card["Marathi"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data1 = pd.DataFrame(to_learn)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Marathi-English Dictionary")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
