import random
from tkinter import *

# ---------------------------- const ------------------------------- #
TEXT = "Who is driving tonight? "
FONT = ("Ariel",20, "italic")
SAMPLE = ["Orel", "Orel"]


# ---------------------------- functions ------------------------------- #
def date():
    canvas.itemconfig(text_date, text = f"The driver is: {random.choice(SAMPLE)}")
    Red_button["state"] = DISABLED
    window.after(3000,another_chance)

def another_chance():
    canvas.itemconfig(text_date, text=TEXT)
    Red_button["state"] = NORMAL


# ---------------------------- window ------------------------------- #
window = Tk( )
window.config(padx=50,pady=50,bg="red")
window.title("random choice".title())
window.minsize(width=500,height=500)

# ---------------------------- canvas ------------------------------- #
canvas = Canvas(width= 400,height=250,highlightthickness=0,bg = "red")
green_screem_img = PhotoImage(file ="green_screem.png")
canvas.create_image(200, 125, image = green_screem_img)
text_date = canvas.create_text(200, 125, text=TEXT, font = FONT, width=200)
canvas.pack()

# ---------------------------- Red_button ------------------------------- #
Red_button_img = PhotoImage(file ="Red_button.png")
Red_button = Button(image = Red_button_img,highlightthickness=0,command=date,bg = "black")
Red_button.pack()



window.mainloop()






