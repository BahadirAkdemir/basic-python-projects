from turtle import Turtle
from turtle import Screen
from turtle import colormode
import random
turtle = Turtle()
colors = ["red", "blue", "green", "yellow", "orange", "purple","CornflowerBlue","DarkOrchid"]
directions = [0,90,180,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_col=(r,g,b)
    return random_col
colormode(255)
turtle.shape("turtle")
turtle.color("green")
screen = Screen()
turtle.pensize(1)
turtle.speed(0)
angle=0
for i in range(1,74):
    turtle.setheading(angle)
    angle+=5
    turtle.color(random_color())
    turtle.circle(100)

screen.exitonclick()
