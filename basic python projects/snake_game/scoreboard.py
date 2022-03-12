from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,350)
        self.score=0
        self.color("white")
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))


    def update(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",30,"normal"))