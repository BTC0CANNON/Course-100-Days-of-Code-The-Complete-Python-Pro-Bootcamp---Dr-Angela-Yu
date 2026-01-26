from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
# ~ timmy.width(15)
timmy.speed("fastest")
# ~ timmy.color("DarkGoldenrod3")

'''Draw a square'''
# ~ for _ in range(4):
	# ~ timmy.forward(100)
	# ~ timmy.right(90)
	
'''Draw dashed lines'''
# ~ for _ in range(10):
	# ~ timmy.forward(10)
	# ~ timmy.penup()
	# ~ timmy.forward(5)
	# ~ timmy.pendown()
	
'''Draw a 3 sided to 10 sided shape, each being a different color'''
def random_hex_color():
    return '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))

'''Long way'''
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(3):
	# ~ timmy.forward(100)
	# ~ timmy.right(120)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(4):
	# ~ timmy.forward(100)
	# ~ timmy.right(90)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(5):
	# ~ timmy.forward(100)
	# ~ timmy.right(72)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(6):
	# ~ timmy.forward(100)
	# ~ timmy.right(60)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(7):
	# ~ timmy.forward(100)
	# ~ timmy.right(51.42)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(8):
	# ~ timmy.forward(100)
	# ~ timmy.right(45)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(9):
	# ~ timmy.forward(100)
	# ~ timmy.right(40)
	
# ~ timmy.color(random_hex_color())	
# ~ for _ in range(10):
	# ~ timmy.forward(100)
	# ~ timmy.right(36)
	
'''Short way'''
# ~ def draw_shape(num_sides):
	# ~ timmy.color(random_hex_color())
	# ~ angle = 360 / num_sides
	# ~ for _ in range(num_sides):
		# ~ timmy.forward(100)
		# ~ timmy.right(angle)
		
# ~ for shape_side_n in range(3, 11):
	# ~ draw_shape(shape_side_n)
	
'''Random path of different colors'''
# ~ for _ in range(100):
	# ~ timmy.color(random_hex_color())
	# ~ timmy.setheading(random.choice([0, 90, 180, 270]))
	# ~ timmy.forward(25)
	
'''Spirograph'''
for _ in range(100):
	timmy.color(random_hex_color())
	timmy.circle(100)
	timmy.left(3.6)

screen = Screen()
screen.exitonclick()

print(timmy)
