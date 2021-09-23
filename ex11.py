import turtle as tl

def left_circle(length):
    for i in range (1, 360, 5):
        tl.forward(length)
        tl.left(5)

def right_circle(length):
    for i in range (1, 360, 5):
        tl.forward(length)
        tl.right(5)


tl.left(90)
for i in range (5, 15, 1):
    left_circle(i)
    right_circle(i)




