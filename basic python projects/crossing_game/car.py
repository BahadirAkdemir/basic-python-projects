from turtle import Turtle
import random

class Car(Turtle):
    colors=['red','blue','green','yellow','orange','purple']
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.color(random.choice(self.colors))
        self.goto(360, random.randint(-300, 300))