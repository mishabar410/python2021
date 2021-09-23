import turtle

n = int(input())
for i in range(0, n, 1):
	turtle.left(360./n)
	turtle.forward(50)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(50)
	turtle.left(180)


	
turtle.done()

