from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.hit_up = False
        self.hit_down = True
        self.hit_left = True
        self.hit_right = False
        self.x=10
        self.y=10
    
        
    def move(self):
        if self.ycor()==290:
            self.hit_up = True
            self.hit_down = False
        elif self.ycor()==-290:
            self.hit_up = False
            self.hit_down = True
        
        if self.hit_down:
            self.y=10
        elif self.hit_up:
            self.y=-10
        
        if self.hit_right:
            self.x=-10
        elif self.hit_left:
            self.x=10

        self.goto(self.xcor()+self.x,self.ycor()+self.y)