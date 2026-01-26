from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color\n{colors}")
user_bet.lower()

# ~ turtle_1 = Turtle(shape="turtle", "red")
# ~ turtle_2 = Turtle(shape="turtle", "yellow")
# ~ turtle_3 = Turtle(shape="turtle", "blue")
# ~ turtle_4 = Turtle(shape="turtle", "orange")
# ~ turtle_5 = Turtle(shape="turtle", "green")
# ~ turtle_6 = Turtle(shape="turtle", "purple")

# ~ turtle_1.penup()
# ~ turtle_2.penup()
# ~ turtle_3.penup()
# ~ turtle_4.penup()
# ~ turtle_5.penup()
# ~ turtle_6.penup()

# ~ turtle_1.goto(-240, -100)
# ~ turtle_2.goto(-240, -60)
# ~ turtle_3.goto(-240, -20)
# ~ turtle_4.goto(-240, 20)
# ~ turtle_5.goto(-240, 60)
# ~ turtle_6.goto(-240, 100)

y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.goto(x=-240, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)
	
if user_bet:
	is_race_on = True

while is_race_on:
	
	for turtle in all_turtles:
		if turtle.xcor() > 230:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You've won! The {winning_color} turtle is the winner!")
			else:
				print(f"You've lost! The {winning_color} turtle is the winner!")
		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()
