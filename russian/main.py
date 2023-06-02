from tkinter import *
import pandas
import random

background_color = "#B1DDC6"

try:
    data = pandas.read_csv("words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("ruscs.csv") 
    to_learn = original_data.to_dict(orient="records")
else:    
    to_learn = data.to_dict(orient="records")

current_card = {}


def known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index = False)
    
    
    next_card()
    

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["Russian"])
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="black")
    # window.config(bg="#CD3333")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000, func= flip_card)
    

def flip_card():
    # window.config(bg=background_color)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image=card_back) 
    

window = Tk()
window.title("Flashy")
rusflag = PhotoImage(file="Flag_of_Russia.png")
window.config(padx=50, pady=50, background=background_color)
flip_timer=window.after(3000, func= flip_card)


canvas = Canvas(width=800, height=526)

# canvas.create_image(700, 700, image=rusflag)

card_front_img = PhotoImage(file='card_front.png')
card_back = PhotoImage(file='cardbbb.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=background_color, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="wrong.png")
unkown_button = Button(image=cross_img,bg=background_color, highlightthickness=0, command=flip_card)
unkown_button.grid(row=1, column=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, highlightthickness=0, bg=background_color, command=known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()



