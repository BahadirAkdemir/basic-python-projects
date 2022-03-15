BACKGROUND_COLOR = "#B1DDC6"
from email.mime import image
from tkinter import font
import pandas as pd
import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Flash Cards For French")
window.configure(background=BACKGROUND_COLOR)
window.geometry("1000x800")
french = "French"
english = "English"
is_Continue = True


data = pd.read_csv("data/french_words.csv")

front_card_photo = tk.PhotoImage(file="images/card_front.png")
back_card_photo = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(window, width=800, height=560, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image=canvas.create_image(400, 300, image=front_card_photo)


lang_text = canvas.create_text(400,100, text="FR-EN Flash Cards",fill="black", font=("Arial", 40,"bold"))
word_text = canvas.create_text(400,300, text="Let's Start",fill="black", font=("Arial", 40,"bold"))
canvas.grid(row=0, column=0, columnspan=2,padx=100, pady=20)


def save_to_file(french, english):
    try:
        with open("data/learned_words.csv", "r") as file:
            lines = file.read()
    except FileNotFoundError:
        with open("data/learned_words.csv", "w") as file:
            file.write("French,English\n")
    else:
        with open("data/learned_words.csv", "a") as file:
            if not french in lines:
                file.write(french + "," + english + "\n")


def change_card_correct():
    global french, english, is_Continue, tick_button
    if is_Continue:
        save_to_file(french, english)
        french, english = get_random_card(data)
        if len(french) > 0:
            canvas.itemconfig(word_text, text=french,fill="black")
            canvas.itemconfig(lang_text, text="Fr",fill="black")
            canvas.itemconfig(canvas_image, image=front_card_photo)
            window.update()

            def change_back_card(english):
                canvas.itemconfig(word_text, text=english,fill="white")
                canvas.itemconfig(lang_text, text="En",fill="white")
                #change canvas image
                canvas.itemconfig(canvas_image,image=back_card_photo)
                window.update()

            window.after(3000, change_back_card, english)
        else:
            canvas.itemconfig(word_text, text="The End")
            canvas.itemconfig(lang_text, text="Congrats! You have learned all words!")
            canvas.itemconfig(canvas_image, image=front_card_photo)
            window.update()

            is_Continue = False
            tick_button['state'] = 'disabled'
    else:
        tick_button['state'] = 'disabled'

def change_card_false():
    global french, english, is_Continue, wrong_button
    if is_Continue:
        french, english = get_random_card(data)
        if len(french) > 0:
            canvas.itemconfig(word_text, text=french,fill="black")
            canvas.itemconfig(lang_text, text="Fr",filll="black")
            canvas.itemconfig(canvas_image, image=front_card_photo)
            window.update()

            def change_back_card(english):
                canvas.itemconfig(word_text, text=english,fill="white")
                canvas.itemconfig(lang_text, text="En",fill="white")
                #change canvas image
                canvas.itemconfig(canvas_image,image=back_card_photo)
                window.update()
        else:
            canvas.itemconfig(word_text, text="The End")
            canvas.itemconfig(lang_text, text="Congrats! You have learned all words!")
            canvas.itemconfig(canvas_image, image=front_card_photo)
            window.update()

            is_Continue = False
            wrong_button['state'] = 'disabled'

        window.after(3000, change_back_card, english)
    else:
        wrong_button['state'] = 'disabled'





tick_photo = tk.PhotoImage(file="images/right.png")
tick_button = tk.Button(image=tick_photo, command=change_card_correct,borderwidth=0)
tick_button.grid(row=1, column=1)

def get_random_card(data):
    global is_Continue
    index = random.randint(0, len(data) - 1)
    french = data.iloc[index]["French"]
    english = data.iloc[index]["English"]
    lines = ""
    try:
        with open("data/learned_words.csv", "r") as file:
            lines = file.read()
    except FileNotFoundError:
        with open("data/learned_words.csv", "w") as file:
            file.write("French,English\n")
        return french, english
    else:
        if not (lines.count('\n') == 102):
            while french in lines:
                index = random.randint(1, len(data) - 1)
                french = data.iloc[index]["French"]
                english = data.iloc[index]["English"]
            return french, english
        else:
            is_Continue = False
            save_to_file(french, english)
            return '', ''

            
            


    


wrong_photo = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_photo, command=change_card_false,borderwidth=0)
wrong_button.grid(row=1, column=0)





window.mainloop()
