from random import randint
import turtle as tl

tl.penup()
tl.goto(-200, -200)
tl.pendown()
tl.goto(-200, 200)
tl.goto(200, 200)
tl.goto(200, -200)
tl.goto(-200, -200)
tl.penup()

number_of_turtles = 20
steps_of_time_number = 1000

Vx_Vy = []
X_Y = []

pool = [tl.Turtle(shape='circle') for i in range(number_of_turtles)]

for i in range(40):
    Vx_Vy.append(int(randint(-70, 70)))
    X_Y.append(int(randint(-200, 200)))

for i in range(steps_of_time_number):
    for j, unit in enumerate(pool):
        X_Y[j*2] += Vx_Vy[j*2]*0.05
        X_Y[j*2+1] += Vx_Vy[j*2+1]*0.05
        unit.penup()
        unit.goto(X_Y[j*2], X_Y[j*2+1])
        if (X_Y[j*2]>=200 or X_Y[j*2]<=-200):
            Vx_Vy[j*2] *= -1
        if (X_Y[j*2+1]>=200 or X_Y[j*2+1]<=-200):
            Vx_Vy[j*2+1] *= -1