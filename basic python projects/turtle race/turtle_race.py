import turtle as t
import random
y_positions = [-70,-40,-10,20,50,80]
colors = ["red","orange","yellow","green","blue","purple"]
turtle_list=[]

print(f"Which turtle will won? ({colors})")
screen = t.Screen()
bet = screen.textinput("Turtle Race!!","Enter your bet: ")


for i in range(0,6):
    turtle = t.Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-350,y_positions[i])
    turtle_list.append(turtle)

is_true=True
while is_true:
    for turtle in turtle_list:
        turtle.forward(random.randint(1,5))
        if turtle.xcor()>350:
            is_true=False
            new_turtle=t.Turtle(shape="turtle")
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.color(turtle.pencolor())
            new_turtle.write(f"Winner is {turtle.pencolor()}",font=("Arial",30,"bold"))
            if turtle.pencolor()==bet:
                new_turtle.goto(0,-50)
                new_turtle.color("green")
                new_turtle.write("You won!",font=("Arial",30,"bold"))
                break
            else:
                new_turtle.goto(0,-50)
                new_turtle.color("red")
                new_turtle.write("You lost!",font=("Arial",30,"bold"))
                break

t.Screen().exitonclick()