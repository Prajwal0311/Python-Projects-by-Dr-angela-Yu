# import colorgram  as clr
"""To Create  a Tuple Of Rgb Colours"""
# rgb_colors=[]
# colors= clr.extract('damien-hirst-spot.jpg',150)
#
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     tuple1=(r,g,b)
#     rgb_colors.append(tuple1)
# print(rgb_colors)
import random
import turtle

color_list = [(244, 242, 243), (245, 243, 238), (223, 73, 55), (233, 144, 82), (19, 14, 14), (44, 88, 149),
              (231, 245, 238), (150, 66, 86), (214, 231, 238), (228, 221, 102), (124, 170, 200), (121, 167, 130),
              (19, 138, 87), (243, 223, 7), (83, 173, 90), (39, 44, 68), (89, 33, 35), (230, 172, 180), (222, 61, 92),
              (195, 128, 158), (115, 65, 45), (78, 48, 84), (16, 164, 214), (174, 187, 45), (161, 209, 185),
              (146, 209, 234)]

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
turtle.colormode(255)
x_axis = tim.xcor()
y_axis = tim.ycor()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()


for dot_count  in range (1,101):
    tim.pencolor(random.choice(color_list))
    tim.pensize(10)
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if dot_count%10==0:
        tim.left(90)
        tim.penup()
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)




screen.exitonclick()
