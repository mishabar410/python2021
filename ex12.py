import turtle as tl

def big_half_circle():
    for i in range (1, 180, 5):
        tl.forward(7)
        tl.right(5)

def small_half_circle():
    for i in range (1, 180, 5):
        tl.forward(2)
        tl.right(5)


turtle.left(90)
for i in range (10):
    big_half_circle()
    small_half_circle()
