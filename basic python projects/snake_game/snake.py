import imp
from turtle import Turtle

positions=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    turtle_list=[]
    direction="right"
    def __init__(self):
        for i in range(3):
            turtle=Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(positions[i])
            self.turtle_list.append(turtle)
        self.head=self.turtle_list[0]
        self.tail = self.turtle_list[2]


    def move(self):
        for turtle in range(len(self.turtle_list)-1,0,-1):
            new_x=self.turtle_list[turtle-1].xcor()
            new_y=self.turtle_list[turtle-1].ycor()
            self.turtle_list[turtle].goto(new_x,new_y)
        self.head.forward(20)
    
    def left(self):
        if self.head.heading()==UP:
            self.direction="left"
            self.turtle_list[0].left(90)
        elif self.head.heading()==DOWN:
            self.direction="left"
            self.turtle_list[0].right(90)
    
    def right(self):
        if self.head.heading()==UP:
            self.direction="right"
            self.turtle_list[0].right(90)
        elif self.head.heading()==DOWN:
            self.direction="right"
            self.turtle_list[0].left(90)
    
    def up(self):
        if self.head.heading()==LEFT:
            self.direction="up"
            self.turtle_list[0].right(90)
        elif self.head.heading()==RIGHT:
            self.direction="up"
            self.turtle_list[0].left(90)
    
    def down(self):
        if self.head.heading()==LEFT:
            self.direction="down"
            self.turtle_list[0].left(90)
        elif self.head.heading()==RIGHT:
            self.direction="down"
            self.turtle_list[0].right(90)
    
    def delete_snake(self):
        for turtle in self.turtle_list:
            turtle.hideturtle()
    def grow(self):
        x,y = self.tail.xcor(),self.tail.ycor()
        turtle=Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(x,y)
        self.turtle_list.append(turtle)
        self.tail=self.turtle_list[-1]
    
    def isHit(self):
        for i in self.turtle_list[1:]:
            if self.head.xcor()==i.xcor() and self.head.ycor()==i.ycor():
                return True
        return False

        
