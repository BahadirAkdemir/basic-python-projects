# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import tkinter as tk
from tkinter import messagebox
import re

from numpy import piecewise
import password_generator

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = tk.Canvas(window, width=200, height=200,highlightthickness=0)
photo = tk.PhotoImage(file="Tkinter password manager/logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)


website_label = tk.Label(text="Website")
website_label.grid(row=1, column=0)

email_username_label = tk.Label(text="Email/Username")
email_username_label.grid(row=2, column=0)

password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0)



website_entry=tk.Entry(width=39)
website_entry.grid(row=1, column=1,columnspan=2)

email_username_entry=tk.Entry(width=39)
email_username_entry.grid(row=2, column=1,columnspan=2)

password_entry=tk.Entry(width=22)
password_entry.grid(row=3, column=1)


def add():
    website=website_entry.get()
    email_username=email_username_entry.get()
    password=password_entry.get()

    if website=="" or email_username=="" or password=="":
        messagebox.showinfo("Error","Please fill all the fields.")
    else:
        if len(re.findall("[\!\@\#\$\%\^\&\*\(\)\_\+\-\=\[\]\|\;\:\,\.\/\<\>\?]",password))<2 or len(re.findall("[0-9]",password))<2 or len(re.findall("[a-zA-Z]",password))<8:
            messagebox.showinfo("Error","Password must contain at least 8 letters, 2 numbers and 2 symbols.")
        else:
            is_correct=messagebox.askokcancel("Password Manager", "Website: "+website+"\nEmail/Username: "+email_username+"\nPassword: "+password)

            if is_correct:
                with open("Tkinter password manager/data.txt","a") as f:
                    f.write(f"{website} | {email_username} | {password}\n")
                website_entry.delete(0,tk.END)
                email_username_entry.delete(0,tk.END)
                password_entry.delete(0,tk.END)

def get_password():
    password=password_generator.get_password()
    password_entry.delete(0,tk.END)
    password_entry.insert(0,password)

generate_password_button = tk.Button(text="Generate Password",command=get_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add",width=37,command=add)
add_button.grid(row=4, column=1,columnspan=2)






window.mainloop()


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #