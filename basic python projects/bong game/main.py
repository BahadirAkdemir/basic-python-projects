import imp
from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
ball = Ball()
left_score=0
right_score=0
scoreboard=Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.write(f"{left_score}  :  {right_score}",align="center",font=("Courier",24,"normal"))
screen.tracer(0)
paddle_left = Paddle(-350,"w","s",screen)
paddle_right = Paddle(350,"Up","Down",screen)

screen.listen()
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")

is_game_on=True
second=0.05
while is_game_on:
    if left_score==5 or right_score==5:
        is_game_on=False
        break
    time.sleep(second)
    if ball.distance(paddle_left)<50 and ball.xcor()<-320:
        ball.hit_left=True
        ball.hit_right=False
        second-=0.005
    elif ball.distance(paddle_right)<50 and ball.xcor()>320:
        ball.hit_right=True
        ball.hit_left=False
        second-=0.005

    if ball.xcor()>400:
        ball.goto(0,0)
        left_score+=1
        scoreboard.clear()
        scoreboard.write(f"{left_score}  :  {right_score}",align="center",font=("Courier",24,"normal"))
        second=0.05
        time.sleep(1)
    if ball.xcor()<-400:
        ball.goto(0,0)
        right_score+=1
        scoreboard.clear()
        scoreboard.write(f"{left_score}  :  {right_score}",align="center",font=("Courier",24,"normal"))
        second=0.05
        time.sleep(1)
    ball.move()
    screen.update()
    
if left_score==5:
    scoreboard.goto(0,20)
    scoreboard.write("Left Player Wins!",align="center",font=("Courier",24,"normal"))
elif right_score==5:
    scoreboard.goto(0,20)
    scoreboard.write("Right Player Wins!",align="center",font=("Courier",24,"normal"))











screen.exitonclick()