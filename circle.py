import turtle

def draw_square(turtle2):
	for i in range(1,5):
		turtle2.forward(100)
		turtle2.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)
	
draw_art()
