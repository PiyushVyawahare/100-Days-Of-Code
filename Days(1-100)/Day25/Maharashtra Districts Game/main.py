import turtle
import pandas

screen = turtle.Screen()
screen.title("Maharashtra State Game")
image = "maharashtra-states.gif"
screen.setup(800, 650)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("35-districts.csv")
all_districts = data.District.to_list()

guessed_districts = []

while len(guessed_districts) < 35:

    answer_district = screen.textinput(title=f"{len(guessed_districts)}/35 Districts Correct",
                                       prompt="What's the next District's name?").title()

    if answer_district == "Exit":
        missing_districts = [district for district in all_districts if district not in guessed_districts]
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")
        break

    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.District == answer_district]
        t.goto(int(district_data.X), int(district_data.Y))
        t.write(answer_district)

