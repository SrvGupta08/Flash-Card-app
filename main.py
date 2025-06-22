# Flash Card App to learn Hindi well

import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
correct_word = {}
data_dict = {}

#---------------------------------- READING DATA FILE -------------------------------------#
try:
    data = pandas.read_csv("./Words to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./hindi_words.csv")
    data_dict = original_data.to_dict(orient = "records")
else:
    data_dict = data.to_dict(orient = "records")

#---------------------------------- WORD GENERTOR -------------------------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text = "Hindi", fill = "black")
    canvas.itemconfig(card_word, text = current_card["Hindi"], fill = "black")
    canvas.itemconfig(card_background, image = card_front)

    window.after(3000, func = flip_card)

#---------------------------------------- FLIPPING OF THE CARD ----------------------------------------#

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back)

#---------------------------------------- KEEPING TRACK OF CORRECT GUESS ----------------------------------------#

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("./Words to learn.csv", index = False)
    next_card()

#---------------------------------------- UI ----------------------------------------#

# Setting up the UI
window = tkinter.Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

# Creating the canvas
canvas = tkinter.Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)

# Creating the front card
card_front = tkinter.PhotoImage(file = "./card_front.png")
card_background = canvas.create_image(400, 263, image = card_front)
canvas.grid(row = 0, column = 0, columnspan = 2)

# Creating the back card
card_back = tkinter.PhotoImage(file = "./card_back.png")

# Creating the title 'Hindi'
card_title = canvas.create_text(410, 150, text = "", font = ("Ariel", 40, "italic"))

# Creating the word 'Hindi Word'
card_word = canvas.create_text(410, 263, text = "", font = ("Ariel", 60, "bold"))

# Creating the wrong button '❌'
wrong_image = tkinter.PhotoImage(file = "./wrong.png")
wrong_button = tkinter.Button(image = wrong_image, highlightthickness = 0, command = next_card)
wrong_button.grid(row = 1, column = 0)

# Creating the right button '✔'
right_image = tkinter.PhotoImage(file = "./right.png")
right_button = tkinter.Button(image = right_image, highlightthickness = 0, command = is_known)
right_button.grid(row = 1, column = 1)

next_card()

window.mainloop()
