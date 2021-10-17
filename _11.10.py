import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((300, 300))

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

        def draw(self, surface):
            circle(surface, self.color, (self.x, self.y), self.r)

        def move(self):
            if(self.x + self.r > 300 or self.x - self.r < 0):
                self.v_x *= -1
            if(self.y + self.r > 300 or self.y - self.r < 0):
                self.v_y *= -1
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




fresh_balls = list()

sonic_rings = list()

for i in range(10):
    tmp_ball = ball()
    fresh_balls.append(tmp_ball)
    fresh_balls[i].init()

for i in range(10):
    tmp_ball = ring()
    sonic_rings.append(tmp_ball)
    sonic_rings[i]()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

count = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(10):
                if (abs(event.pos[0] - fresh_balls[i].x) < fresh_balls[i].r and abs(event.pos[1] - fresh_balls[i].y) < fresh_balls[i].r):
                    count +=1
                    print(count)
                if (abs(event.pos[0] - sonic_rings[i].x) < sonic_rings[i].r and abs(event.pos[1] - sonic_rings[i].y) < sonic_rings[i].r):
                    count +=5
                    f1 = pygame.font.Font(None, 36)
                    text1 = f1.render('Hello Привет', True, (180, 0, 0))
                    print(count)
    for i in range(10):
        fresh_balls[i].move()
        fresh_balls[i].draw(screen)

        sonic_rings[i].move()
        sonic_rings[i].draw(screen)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()