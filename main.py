# import colorgram
#
# colors = colorgram.extract("spot painting.jpg", 25)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle as t
from turtle import Screen

t.colormode(255)
tim = t.Turtle()

color_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205),
              (109, 67, 85), (39, 35, 34), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47),
              (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186),
              (150, 180, 170), (90, 143, 158), (28, 81, 59)]


tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for x in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
