import turtle as tl

def star(n):
    angle = (360 * (n-2)/n)/(2*(n-2))
    for i in range(n): 
        tl.forward(100)
        tl.left(180-angle)

n = int(input())
star(n)