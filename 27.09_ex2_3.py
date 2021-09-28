import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 300))

polygon(screen, (161, 235, 245), [(0, 65), (700, 65)], 150)
polygon(screen, (14, 147, 37), [(0, 215), (700, 215)], 150)

big_n_polygon = list()
small_npolygon = list()

def polygons(big_n_polygon, small_npolygon, x, y, R):
    tmp_1 = tuple()
    tmp_2 = tuple()
    for i in range(20):
        tmp_1 = (x + R * math.cos(2 * math.pi * i/20)), (y + R * math.sin(2 * math.pi * i/20))
        tmp_2 = (x + 0.9 * R * math.cos(2 * math.pi / 40 + 2 * math.pi * i/20)), (y + 0.9 * R * math.sin(2 * math.pi / 40 + 2 * math.pi * i/20))
        big_n_polygon.append(tmp_1)
        small_npolygon.append(tmp_2)

def house(x, y, k):
    polygon(screen, (0, 0, 0), [(x - 2, y + 2), (x+110.0*k + 2, y + 2), (x + 110.0 * k + 2,y + 75.0 * k - 2), (x - 2, y + 75.0 * k - 2)])
    a = 110.0 * k
    b = 75.0 * k
    polygon(screen, (147, 107, 14), [(x, y), (x + 110.0 * k, y), (x+110.0*k,y+75.0*k), (x, y+75.0*k)])
    polygon(screen, (235, 47, 68), [(x + a, y), (x, y), (x + a/2, y - 0.5*b)])
    polygon(screen, (181, 98, 17), [(x + 38.0 * k, y + 40.0 * k), (x + 77.0 * k, y + 40.0 * k)], int(32 * k))
    polygon(screen, (14, 147, 145), [(x + 40.0 * k, y + 40.0 * k), (x + 75.0 * k, y + 40.0 * k)], int(30 * k))

def clouds(x, y, k):
    for i in range(2):
        circle(screen, (0, 0, 0), (x + i * int(15 * k), y), int(15 * k))
        circle(screen, (255, 255, 255), (x + i * int(15 * k), y), int(14 * k))

    for i in range (4):
        circle(screen, (0, 0, 0), (x + i * int(15 * k) - 15, y + 15), int(15 * k))
        circle(screen, (255, 255, 255), (x + i * int(15 * k) - 15, y + 15), int(14 * k))

def tree(x, y, k):
    #x=335 y=140
    polygon(screen, (0, 0, 0), [(x-5 * k, y), (x-5 * k, y + 50 * k), (x+5 * k, y + 50 * k), (x+5, y)])

    circle(screen, (0, 0, 0), (x - 15 * k, y - 5 * k), int(15 * k))
    circle(screen, (15, 83, 14), (x - 15 * k, y - 5 * k), int(14 * k))

    circle(screen, (0, 0, 0), (x - 15 * k, y - 20 * k), int(15 * k))
    circle(screen, (15, 83, 14), (x - 15 * k, y - 20 * k), int(14 * k))

    circle(screen, (0, 0, 0), (x, y - 13 * k), int(15 * k))
    circle(screen, (15, 83, 14), (x, y - 13 * k), int(14 * k))

    circle(screen, (0, 0, 0), (x, y - 28 * k), int(15 * k))
    circle(screen, (15, 83, 14), (x, y - 28 * k), int(14 * k))

    circle(screen, (0, 0, 0), (x + 20 * k, y - 5 * k), int(15 * k))
    circle(screen, (15, 83, 14), (x + 20 * k, y - 5 * k), int(14 * k))

    circle(screen, (0, 0, 0), (x + 20 * k, y - 20 * k), int(15 * k))
    circle(screen, (15, 83, 14), (x + 20 * k, y - 20 * k), int(14 * k))

    '''
    polygon(screen, (0, 0, 0), [(330, 140), (330, 190), (340, 190), (340, 140)])

    circle(screen, (0, 0, 0), (320, 135), 15)
    circle(screen, (15, 83, 14), (320, 135), 14)

    circle(screen, (0, 0, 0), (320, 120), 15)
    circle(screen, (15, 83, 14), (320, 120), 14)

    circle(screen, (0, 0, 0), (335, 127), 15)
    circle(screen, (15, 83, 14), (335, 127), 14)

    circle(screen, (0, 0, 0), (335, 112), 15)
    circle(screen, (15, 83, 14), (335, 112), 14)

    circle(screen, (0, 0, 0), (350, 135), 15)
    circle(screen, (15, 83, 14), (350, 135), 14)

    circle(screen, (0, 0, 0), (350, 120), 15)
    circle(screen, (15, 83, 14), (350, 120), 14)
    

house(70, 125, 1)

house(270, 125, 1.5)

clouds(143, 40, 1)

clouds(243, 40, 1.5)

tree(335, 140, 1)
'''

tree(400, 140, 1)

clouds(300, 75, 1)

house(100, 145, 1)

polygons(big_n_polygon, small_npolygon, 500, 75, 20)

total = list()

for i in range(20):
    total.append(big_n_polygon[i])
    total.append(small_npolygon[i])

polygon(screen, (249, 194, 194), total)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
