import pandas as pd
import turtle

data = pd.read_csv('us_states_quiz_game/50_states.csv')
states_list = list(data['state'])
screen = turtle.Screen()
screen.title("US State Quiz")
image_path = "us_states_quiz_game/blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)   

count=0
while count<50:
    input = screen.textinput("", "State Name: ")
    if input.title() in states_list:
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(int(data[data["state"]==input.title()]["x"]), int(data[data["state"]==input.title()]["y"]))
        new_turtle.write(input.title(), font=("Arial", 10, "bold"))
        count+=1




screen.exitonclick()
 