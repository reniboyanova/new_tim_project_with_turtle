import turtle
from turtle import Turtle, Screen
import random

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red',]


screen = Screen()


screen.setup(width=500, height=400)
the_game_is_on = False
user_bet = screen.textinput(title='Make your bet', prompt='Please type the color of the turtle that you think will win: ')
x_coordinate = -230
y_coordinate = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_coordinate, y=y_coordinate[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    the_game_is_on = True


while the_game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            the_game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} completed the rase first!")
            else:
                print(f"You lost! The {winning_color} completed the rase first!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
