# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as t
t.colormode(255)
tim = t.Turtle()

color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen = t.Screen()
screen.exitonclick()
