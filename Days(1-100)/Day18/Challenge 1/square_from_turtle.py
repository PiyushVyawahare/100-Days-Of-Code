from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle ")
tim.color("blue", "red")
tim.color("blue", "red")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()