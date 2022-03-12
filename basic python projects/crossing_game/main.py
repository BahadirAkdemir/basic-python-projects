from car import Car
from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.tracer(0)
screen.screensize(500, 500)
screen.bgcolor("white")
turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.setheading(90)
turtle.speed(0)
turtle.goto(0, -330)
screen.listen()

def up():
    turtle.forward(10)


def down():
    turtle.backward(10)

screen.onkey(up, "Up")
screen.onkey(down, "Down")

is_game_over = False
car_list = []

while is_game_over is False:
    time.sleep(0.1)
    screen.update()
    rand_num = random.randint(1, 5)
    create_car = random.choice([True, False, False])

    if create_car:
        for i in range(rand_num):
            car = Car()
            car_list.append(car)
    
    for i in car_list:
        i.goto(i.xcor() -10, i.ycor())
        if turtle.distance(i) < 20:
            is_game_over = True
            print("Game Over!")
            break

        

    if turtle.ycor() > 330:
        is_game_over = True
        print("Winner!")

screen.exitonclick()
