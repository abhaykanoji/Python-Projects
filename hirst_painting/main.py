import turtle as t
import random
color_list =[(202, 166, 109), (240, 246, 241), (236, 239, 244), (153, 73, 47), (170, 152, 42), (222, 202, 137),
(53, 93, 124), (136, 32, 22), (133, 163, 184), (48, 118, 87), (199, 92, 71), (16, 97, 75),(101, 73, 75), (67, 47, 41),
(147, 178, 148), (164, 142, 156), (234, 177, 165), (56, 46, 49), (130, 28, 32), (184, 205, 173), (41, 60, 72),
(81, 146, 125), (184, 87, 92), (31, 78, 84), (48, 64, 81), (21, 69, 63),(219, 175, 178), (109, 124, 150)]


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
