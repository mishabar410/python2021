import turtle

def circle():
	for i in range(0, 360, 5):
		turtle.forward(2)
		turtle.left(5)

for i in range (0, 8, 1):
	circle()
	turtle.left(360/8)
		
turtle.done()

