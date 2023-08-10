from tkinter import *
from pandas import *
from random import *


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
DELAY = 5000

# ---------------------------- GAME LOGIC ------------------------------- #

current_pair = {}
to_learn = {}

try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    org_data = read_csv("./data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def gen_card():
    global current_pair, after_id

    window.after_cancel(after_id)

    current_pair = choice(to_learn)
    canvas.itemconfig(canvas_image, image=img_card_front)
    canvas.itemconfig(text_word, text=current_pair["French"], fill="black")
    canvas.itemconfig(text_title, text="French", fill="black")
    after_id = window.after(DELAY, func=flip_card)


def flip_card():
    global current_pair

    canvas.itemconfig(canvas_image, image=img_card_back)
    canvas.itemconfig(text_word, text=current_pair["English"], fill="white")
    canvas.itemconfig(text_title, text="English", fill="white")


def known_card():
    to_learn.remove(current_pair)
    DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)
    gen_card()


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
after_id = window.after(DELAY, func=flip_card)

# Canvas

img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=img_card_front)
text_title = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
text_word = canvas.create_text(400, 250, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button

img_right = PhotoImage(file="./images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=known_card)
button_right.grid(column=1, row=1)

img_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=gen_card)
button_wrong.grid(column=0, row=1)

gen_card()

window.mainloop()
