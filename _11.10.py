import pygame
import json
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((300, 500))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class ball:

        def init(self):
            self.x = randint(100, 200)
            self.y = randint(100, 200)
            self.v_x = randint(-150, 150)
            self.v_y = randint(-150, 150)
            self.r = randint(5, 20)
            self.color = COLORS[randint(0, 5)]

        def collision(self):
            if(self.x + self.r > 300 or self.x - self.r < 0):
                self.v_x *= -1
            if(self.y + self.r > 300 or self.y - self.r < 0):
                self.v_y *= -1

        def draw(self, surface):
            circle(surface, self.color, (self.x, self.y), self.r)

        def move(self):
            self.x += self.v_x * 0.01
            self.y += self.v_y * 0.01

class ring:
    def __init__(self):
        self.x = randint(100, 200)
        self.y = randint(100, 200)
        self.v_x = randint(-150, 150)
        self.v_y = randint(-150, 150)
        self.R = randint(10, 15)
        self.r = randint(self.R - 7, self.R - 3)
        self.color = COLORS[randint(0, 5)]

    def draw(self, surface):
            random = randint(0, 100)
            if random < 50:
                circle(surface, BLACK, (self.x, self.y), self.R)
            else:
                circle(surface, self.color, (self.x, self.y), self.R)
                circle(surface, BLACK, (self.x, self.y), self.r)

    def move(self):
            if(self.x + self.r > 300 or self.x - self.r < 0):
                self.v_x *= -1
            if(self.y + self.r > 300 or self.y - self.r < 0):
                self.v_y *= -1
            self.x += self.v_x * 0.01
            self.y += self.v_y * 0.01

def draw_heart(surface, color, x, y, width, height):
    polygon(surface, color, [(x + width // 20, y + height // 4), 
                             (x + width // 2, y + height), 
                             (x + width * 19 // 20, y + height // 4)])
    circle(surface, color, (x + width * 3 // 10, y + height // 4), width // 4)
    circle(surface, color, (x + width * 7 // 10, y + height // 4), width // 4)

def draw_life_screen(hearts, count):
    polygon(screen, WHITE, [(0, 300), (300, 300), (300, 500), (0, 500)])
    
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(count), False, BLACK)
    screen.blit(textsurface, (50, 305))

    textsurface = myfont.render(str(hearts), False, BLACK)
    screen.blit(textsurface, (50, 350))
    draw_heart(screen, RED, 75, 345, 50, 50) 

fresh_balls = list()

sonic_rings = list()

for i in range(10):
    tmp_ball = ball()
    fresh_balls.append(tmp_ball)
    fresh_balls[i].init()

for i in range(10):
    tmp_ball = ring()
    sonic_rings.append(tmp_ball)
    sonic_rings[i].__init__()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

count = 0
tmp_count = 0
tmp_hearts = 2
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(10):
                if (abs(event.pos[0] - fresh_balls[i].x) < fresh_balls[i].r and 
                    abs(event.pos[1] - fresh_balls[i].y) < fresh_balls[i].r):
                    tmp_count +=1
                    print(count)
                elif (abs(event.pos[0] - sonic_rings[i].x) < sonic_rings[i].r and 
                      abs(event.pos[1] - sonic_rings[i].y) < sonic_rings[i].r):
                    tmp_count +=5
                    print(count)
            if (tmp_count == 0):
                tmp_hearts = tmp_hearts - 1
            if (tmp_hearts  == -1):
                finished = True
            count += tmp_count
            tmp_count = 0
                
    for i in range(10):
        fresh_balls[i].collision()
        fresh_balls[i].move()
        fresh_balls[i].draw(screen)

        sonic_rings[i].move()
        sonic_rings[i].draw(screen)

    draw_life_screen(tmp_hearts, count)
    pygame.display.update()
    screen.fill(BLACK)

with open("records.json", 'r') as f:
    records = json.load(f)

name = input()
records.append({"name" : name, "points" : count})

records = sorted(records, key = lambda x: x["points"])

with open("records.json", 'w') as f:
    json.dump(records, f)

pygame.quit()