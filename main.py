from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("road.gif")
ALIGN = "right"
FONT = ("Courier", 28, "bold")

y_position = [-260, -172, -85, 2, 85, 172, 260]
colors = ["yellow", "green", "black", "white", "pink", "red", "blue"]
all_tutles = []

for index in range(0, 7):
    new_tur = Turtle(shape="turtle")
    new_tur.shapesize(2)
    new_tur.speed('fastest')
    new_tur.penup()
    new_tur.goto(x=-350, y=y_position[index])
    new_tur.color(colors[index])
    all_tutles.append(new_tur)

is_one = True

while is_one:
    user_bet = screen.textinput('Enter your bet', prompt='Which turtle (color): ')

    if user_bet not in colors:
        user_bet = screen.textinput('Erorr', prompt='Please enter your value')
        continue

    while is_one:
        for turtle in all_tutles:
            if turtle.xcor() > 330:
                is_one = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    turtle.write(f'Winner! The {winner} is winner', font=FONT, align=ALIGN)
                else:
                    turtle.write(f'Lost! The {winner} is winner', font=FONT, align=ALIGN)
            random_race = random.randint(0, 20)
            turtle.forward(random_race)

screen.exitonclick()
