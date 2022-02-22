from turtle import Turtle, Screen
import random
import turtle
#from color import rgb_colors


rgb_colors = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182)]

turtle.colormode(255)
t = Turtle()
s = Screen()

t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 100

for count in range(1, num_of_dots+1):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)

    if count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s.exitonclick()
