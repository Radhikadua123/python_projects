import turtle

def draw_square():
	window=turtle.Screen()
	window.bgcolor("yellow")

	pointer=turtle.Turtle()
	pointer.forward(100)
	pointer.right(90)
	pointer.forward(100)
	pointer.right(90)
	pointer.forward(100)
	pointer.right(90)
	pointer.forward(100)
	pointer.right(90)
	
	window.exitonclick()

draw_square()
