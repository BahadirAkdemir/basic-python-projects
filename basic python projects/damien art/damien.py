#import colorgram


#colors=colorgram.extract("lahana.jpeg",38)
rgb_colors=[(253, 252, 241), (238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176), (87, 22, 58), (182, 188, 209), (118, 122, 149), (94, 16, 15)]

import turtle as t
import random
turtle = t.Turtle()
turtle.hideturtle()
t.colormode(255)
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)

for _ in range(10):
    for i in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)

t.Screen().exitonclick()
