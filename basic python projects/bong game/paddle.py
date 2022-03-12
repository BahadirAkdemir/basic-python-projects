from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,up,down,screen):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x,0)
    
    def go_up(self):
            if self.ycor()>-260 and self.ycor()+20<260:
                ycor=self.ycor()+20
                self.goto(self.xcor(),ycor)
    def go_down(self):
        if self.ycor()-20>-260 and self.ycor()<260:
            ycor=self.ycor()-20
            self.goto(self.xcor(),ycor)
        
        
        
        
