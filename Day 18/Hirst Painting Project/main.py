from turtle import Turtle, Screen
import turtle
import random
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
turtle.colormode(255)
screen = Screen()
screen.setup(width=1000, height=1000)
timmy.goto(-450, -450)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	new_color = (r, g, b)
	rgb_colors.append(new_color)
	
def go_forward(): 
	for _ in range(9):
		rgb_choice = random.choice(rgb_colors)
		timmy.dot(40, rgb_choice)
		timmy.forward(100)
		
def turn_left_go_up():
	rgb_choice = random.choice(rgb_colors)
	timmy.dot(40, rgb_choice)
	timmy.left(90)
	timmy.forward(100)
	timmy.left(90)
	
def turn_right_go_up():
	rgb_choice = random.choice(rgb_colors)
	timmy.dot(40, rgb_choice)
	timmy.right(90)
	timmy.forward(100)
	timmy.right(90)

for _ in range(5):
	go_forward()
	turn_left_go_up()
	go_forward()
	turn_right_go_up()

screen.exitonclick()

print(timmy)
