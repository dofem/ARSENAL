from tkinter import *
import pandas
from random import *
BACK_GROUND = "#FF0000"
current_num = {}
CARD_BACK = "#FFCC70"

try:
    data = pandas.read_csv("DATA/squad_to_know.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("DATA/ARSENAL_PLAYER.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")
    print(learn)


def new_number():
    global current_num, flip_timer
    window.after_cancel(flip_timer)
    current_num = choice(learn)
    canvas.itemconfig(Squad_no, text="Squad Number", fill="black")
    canvas.itemconfig(number, text=current_num["SQUAD_NO"], fill="black")
    canvas.itemconfig(front_image, image=card_front,)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(Squad_no, text="Player Name", fill="red")
    canvas.itemconfig(number, text=current_num["PLAYER_NAME"], fill="red")


def is_known():
    learn.remove(current_num)
    data = pandas.DataFrame(learn)
    data.to_csv("DATA/squad_to_know.csv", index=False)
    new_number()


window = Tk()
window.title("ARSENAL PLAYERS")
window.config(padx=50, pady=50, bg=BACK_GROUND)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=560)
card_front = PhotoImage(file="IMAGE/card_front.png")
front_image = canvas.create_image(400, 280, image=card_front)
canvas.config(bg=BACK_GROUND, highlightthickness=0)
Squad_no = canvas.create_text(400, 120, text="Squad Number", font=("Ariel", 30, "italic"))
number = canvas.create_text(400, 300, text="Number", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="IMAGE/wrong.png")
check_image = PhotoImage(file="IMAGE/right.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_number)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

new_number()

window.mainloop()