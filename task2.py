import turtle as tl

def draw_1():
    tl.right(90)
    tl.forward(20)
    tl.pendown()
    tl.left(135)
    tl.forward(((20**2)*2)**0.5)
    tl.right(135)
    tl.forward(40)
    tl.left(90)
    tl.penup()

def draw_4():
    tl.pendown()
    tl.right(90)
    tl.forward(20)
    tl.left(90)
    tl.forward(20)
    tl.left(90)
    tl.forward(20)
    tl.left(180)
    tl.forward(40)
    tl.left(90)
    tl.penup()

def draw_7():
    tl.pendown()
    tl.forward(20)
    tl.right(135)
    tl.forward(((20**2)*2)**0.5)
    tl.left(45)
    tl.forward(20)
    tl.left(90)

    tl.penup()

def draw_0():
    tl.pendown()
    tl.forward(20)
    tl.right(90)
    tl.forward(40)
    tl.right(90)
    tl.forward(20)
    tl.right(90)
    tl.forward(40)
    tl.right(90)
    tl.penup()


# index = input()
index = '0123456789'
dict_1 = {
    '1' : [(0,-20), (20, 0), (20, -40)],
    '2' : [(0, 0), (20, 0), (20, -20), (0, -40), (20, -40)],
    '3' : [(0, 0), (20, 0), (0, -20), (20, -20), (0, -40)],
    '4' : [(0, 0), (0, -20), (20, -20), (20, 0), (20, -40)],
    '5' : [(20, 0), (0, 0), (0, -20), (20, -20), (20, -40), (0, -40)],
    '6' : [(20, 0), (0, 0), (0, -20), (20, -20), (20, -40), (0, -40), (0, -20)],
    '7' : [(0, 0), (20, 0), (0, -20), (0, -40)],
    '8' : [(20, 0), (0, 0), (0, -20), (20, -20), (20, 0), (20, -40), (0, -40), (0, -20)],
    '9' : [(20, 0), (0, 0), (0, -20), (20, -20), (20, 0), (20, -20), (0, -40)],
    '0' : [(0,0), (20, 0), (20, -40), (0, -40), (0,0)]
}   

for i, ind_num in enumerate(index):
    for j, coords in enumerate(dict_1[ind_num]):
        if (j==0): 
            tl.penup()
        else: 
            tl.pendown()
        tl.goto(coords[0]+25*i, coords[1])