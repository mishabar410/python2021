import turtle

def n_polygon(n, length):
	for i in range(0, n, 1):
		turtle.left(360./n)
		turtle.forward(length)
	
#turtle.left(30)
for i in range(3, 13, 1):
	length = i*5
	n_polygon(i, length)
	turtle.right(90)
	turtle.penup()
	turtle.forward(length/3)
	turtle.pendown()
	turtle.left(90)
	
turtle.done()

