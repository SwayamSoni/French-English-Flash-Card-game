from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data_file = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("French_words.csv")
print(data_file)
data = data_file.to_dict(orient="records")



def words_learned():
    global data,selected
    data_corrected = [d for d in data if d.get('English') != selected["English"]]
    data = data_corrected
    print(len(data))
    df = pandas.DataFrame(data, columns=["French", "English"])
    df.to_csv("words_to_learn.csv", index=False)
    next_card()


def eng_card():

    canvas.itemconfig(canvas_image,image= card_back_img)
    Title_label.config(text='English',highlightthickness=0,bg="#91C2AF",fg="white")
    Word_label.config(text= selected['English'],highlightthickness=0,bg="#91C2AF",fg="white")

def next_card():

    global selected,timer

    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=card_front_img)
    Title_label.config(text='French',bg="white",fg="black")
    selected = random.choice(data)
    Word_label.config(text = selected['French'],bg="white",fg="black")
    timer = window.after(3000,func=eng_card)





window = Tk()
window.title("Flashy")
window.config(padx = 50,pady = 50,bg= BACKGROUND_COLOR,highlightthickness=0)



canvas = Canvas(width = 800, height = 526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file = "card_front.png")
card_back_img = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image( 400,263,image = card_front_img)
canvas.grid(row = 0,column = 0,columnspan=2)

Title_label = Label(text="",font=("Ariel",40,"italic"),bg = "white")
Title_label.place(x=400,y=150,anchor="center")

Word_label = Label(text="",font=("Ariel",60,"bold"),bg = "white")
Word_label.place(x=400,y=263,anchor="center")

timer = window.after(3000,func=eng_card)
next_card()

right_img = PhotoImage(file = "right.png")
r_button = Button(image=right_img,highlightthickness=0,bg=BACKGROUND_COLOR,command=words_learned)
r_button.grid(row = 1,column = 1)

wrong_img = PhotoImage(file = "wrong.png")
w_button = Button(image=wrong_img,highlightthickness=0,bg=BACKGROUND_COLOR,command=next_card)
w_button.grid(row = 1,column = 0)




window.mainloop()


