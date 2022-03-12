
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

import tkinter as tk
import time

window = tk.Tk()
window.title("Pomodoro Timer")
window.config(bg=PINK,padx=100,pady=150)


canvas = tk.Canvas(window, width=500, height=500, bg=PINK,highlightthickness=0)
photo = tk.PhotoImage(file="Tkinter Pomodoro App/tomato.png")
canvas.create_image(250, 250, image=photo)
timer_text = canvas.create_text(250,270, text="00.00",fill="white", font=(FONT_NAME, 40,"bold"))
canvas.grid(row=1, column=1)

label = tk.Label(text="TIMER",fg=GREEN,bg=PINK,font=(FONT_NAME, 40,"bold"))
label.grid(row=0, column=1)

is_continue = True

def start():
    button1['state'] = 'disabled'
    global REP
    REP += 1
    work=25*60
    short_break=5*60
    long_break=20*60
    if REP%2==1:
        label.configure(text="WORK",fg=GREEN,bg=PINK,font=(FONT_NAME, 40,"bold"))
        start_timer(work)
    elif REP==8:
        REP=0
        label.configure(text="LONG BREAK",fg=RED,bg=PINK,font=(FONT_NAME, 40,"bold"))
        start_timer(long_break)
    elif REP%2==0:
        label.configure(text="SHORT BREAK",fg=RED,bg=PINK,font=(FONT_NAME, 40,"bold"))
        start_timer(short_break)

    

def start_timer(sec):
    global timer
    button2['state'] = 'normal'
    time1=int(sec/60)
    time2=int(sec%60)

    if time1<10:
        time1="0"+str(time1)
    if time2 < 10:
        time2 = "0" + str(time2)
    if sec > 0:
        canvas.itemconfig(timer_text,text=f"{time1}.{time2}")
        timer = window.after(1000,start_timer,sec-1)
    else:
        start()

def end():
    global REP
    window.after_cancel(timer)
    button1['state'] = 'normal'
    button2['state'] = 'disabled'
    canvas.itemconfig(timer_text,text="00.00")
    label.configure(text="TIMER",fg=GREEN,bg=PINK, font=(FONT_NAME, 40,"bold"))
    REP = 0

button1 = tk.Button(text="Start",highlightbackground=PINK,command=start)
button1.grid(row=2, column=0)

button2 = tk.Button(text="End",bg=PINK,highlightbackground=PINK,command=end)
button2.config(bg=PINK)
button2.grid(row=2, column=2)

label_tick = tk.Label(text="✔",fg=GREEN,bg=PINK,font=(FONT_NAME, 40,"bold"))
label_tick.grid(row=2, column=1)







window.mainloop()