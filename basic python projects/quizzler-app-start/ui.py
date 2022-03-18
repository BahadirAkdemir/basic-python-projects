THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

from tkinter import *

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.geometry("350x500")
        self.window.configure(background=THEME_COLOR)
        self.score=0

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_label = self.canvas.create_text(150,125,text="", font=("Arial", 20, "italic"), fill="black",width=290)
        self.score_label = Label(self.window, text=f"Score: {self.score}/10", font=("Arial", 20, "italic"), bg=THEME_COLOR, fg="white",padx=20, pady=20)
        self.true_photo = PhotoImage(file="Images/true.png")
        self.false_photo = PhotoImage(file="Images/false.png")
        self.true_button = Button(self.window, image=self.true_photo, bg=THEME_COLOR, fg="white", command=self.check_answer_true,)
        self.false_button = Button(self.window, image=self.false_photo, bg=THEME_COLOR, fg="white", command=self.check_answer_false)

        self.canvas.grid(row=1, column=0,columnspan=2,padx=20, pady=20)
        self.score_label.grid(row=0, column=1)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.true_button.config(state=NORMAL)
            self.false_button.config(state=NORMAL)
            self.canvas.itemconfig(self.question_label, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.question_label, text="Finished!!")

    def check_answer_true(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        check="False"
        if self.quiz_brain.check_answer() == "True":
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/10")
            check="True"
        self.give_feedback(check)
        self.window.after(1000, self.get_question)

    
    def check_answer_false(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        check="False"
        if self.quiz_brain.check_answer() == "False":
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/10")
            check="True"
        self.give_feedback(check)
        self.window.after(1000, self.get_question)

    def give_feedback(self,check):
        if check == "True":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

