import turtle as tl

def draw_left_circle(length):
    tl.pendown()
    for i in range (1, 360, 5):
        tl.forward(length)
        tl.left(5)
    tl.penup()

def draw_right_circle(length):
    tl.pendown()
    for i in range (1, 360, 5):
        tl.forward(length)
        tl.right(5)
    tl.penup()

def draw_half_circle():
    tl.pendown()
    for i in range (1, 180, 5):
        tl.forward(5)
        tl.right(5)
    tl.penup()

def draw_eyes():
    
    tl.left(90)
    tl.forward(110)
    tl.right(90)
    tl.forward(40)
    tl.left(90)
    tl.forward(20)
    tl.right(90)
    
    tl.color('red')
    tl.begin_fill()
    draw_left_circle(3)
    tl.end_fill()
    
    tl.right(90)
    tl.forward(40)
    tl.left(90)
    
    tl.color('red')
    tl.begin_fill()
    draw_right_circle(3)
    tl.end_fill()

def draw_head():
    tl.penup()
    tl.left(90)
    
    tl.color('yellow')
    tl.begin_fill()
    draw_left_circle(10)
    tl.end_fill()

def draw_nose():
    tl.color('black')
    tl.left(90)
    tl.forward(20)
    tl.left(90)
    tl.pendown()
    tl.width(5)	
    tl.forward(35)
    tl.penup()

def draw_smile():
    tl.color('blue')
    tl.forward(20)
    tl.left(90)
    tl.forward(55)
    tl.right(90)
    tl.width(4)
    draw_half_circle()


draw_head()
draw_eyes()
draw_nose()
draw_smile()


