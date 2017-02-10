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
	
	pointer2=turtle.Turtle()
	pointer2.color("blue")
	pointer2.shape("turtle")
	
	pointer2.circle(100)
	
	window.exitonclick()

draw_square()
