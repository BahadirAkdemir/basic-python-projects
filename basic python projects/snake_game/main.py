from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(False)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


game_is_running=True


screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
while game_is_running:
    if snake.head.xcor()+10>390 or snake.head.xcor()-10<-390 or snake.head.ycor()+10>380 or snake.head.ycor()-10<-380 or snake.isHit():
        game_is_running=False
        scoreboard.game_over()
        ##snake.delete_snake()
        break
    time.sleep(0.1)
    screen.update()
    snake.move()


    if snake.head.distance(food)<15:
        food.move()
        scoreboard.update()
        snake.grow()


    
    
screen.exitonclick()