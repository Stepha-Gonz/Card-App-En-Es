
import pandas as pd
from tkinter import *
from random import choice
BG_COLOR="#B1DDC6"

#,--------------------------------READ FILE -------------------------------------------
try:
    data=pd.read_csv("data/to_learn_words.csv")
except FileNotFoundError:
    origin_data=pd.read_csv("data/english_words.csv")
    data_dict=origin_data.to_dict(orient="records")
else:
    data_dict=data.to_dict(orient="records")
current_card={}


#,-----------------------------------FUNCTIONS------------------------------------------
def next_card():
    global current_card
    current_card=choice(data_dict)
    canvas.itemconfig(canvas_bg,image=front_img)
    canvas.itemconfig(lg_title,text="English",fill="black")
    canvas.itemconfig(word_title,text=current_card["English"],fill="black")
    button_unknown.config(image=wrong_img,command=flip_card)
def flip_card():
    canvas.itemconfig(canvas_bg,image=back_img)
    canvas.itemconfig(lg_title,text="Spanish", fill="white")
    canvas.itemconfig(word_title,text=current_card["Spanish"], fill="white")
    button_unknown.config(image=next_img,command=next_card)
    

def is_known():
    data_dict.remove(current_card)
    data=pd.DataFrame(data_dict)
    to_learn=data.to_csv("data/to_learn_words.csv",index=False)
    next_card()
    


#.window
window=Tk()
window.title("Card App for learning English")
window.config(bg=BG_COLOR, padx=50, pady=50)

#.canvas
canvas=Canvas( width=800, height=526,bg=BG_COLOR, highlightthickness=0)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
canvas_bg=canvas.create_image(400,263,image=front_img)

lg_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word_title=canvas.create_text(400,263,text="Title",font=("Ariel",60,"bold"))



canvas.grid(column=0, row=0, columnspan=3)

#.buttons

check_img=PhotoImage(file="images/right.png")
wrong_img=PhotoImage(file="images/wrong.png")
next_img=PhotoImage(file="images/next.png")

button_known=Button(image=check_img,highlightthickness=0, command=is_known) 
button_known.grid(column=0,row=1)
button_unknown=Button(image=wrong_img,highlightthickness=0,command=flip_card)
button_unknown.grid(column=2, row=1)

next_card()
window.mainloop()