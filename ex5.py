import turtle

for i in range(10, 70, 6):
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.right(90)
	turtle.penup()
	turtle.forward(3)
	turtle.left(90)
	turtle.forward(3)
	turtle.left(90)
	turtle.pendown()
	
turtle.done()

