import turtle as tl

Vx = 10
Vy = 20
ay = -9.81
x = 0
y = 0
for i in range(200):
    x += Vx*0.05
    y += Vy*0.05
    Vy += ay*0.05
    tl.goto(x, y)
    if(y <= 0):
        Vy *= -0.7

