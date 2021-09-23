from turtle import Turtle, Screen

tim = Turtle()

color = ["red", "blue", "green", "silver", "dark olive green", "hot pink", "maroon", "black"]

for i in range(3, 11):
    angle = 360/i
    tim.color(color[i-3])
    
    while i > 0:
        tim.forward(80)
        tim.right(angle)
        i -= 1

screen = Screen()
screen.exitonclick()
