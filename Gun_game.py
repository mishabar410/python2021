import math
from random import choice
from random import randint
import pygame


FPS = 400

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

POINTS = 0
time = 420
name = 'misha'

screen = pygame.display.set_mode((WIDTH, HEIGHT))

global targets
targets = list()

class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def collision(self):
        if(self.x + self.r > 800 or self.x - self.r < 0):
            self.vx *= -0.99
        if(self.y + self.r > 600):
            self.vy *= -0.99

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx * 0.035
        self.y -= self.vy * 0.035
        self.vy -= 10 * 0.035
        self.live -= 0.01
        if(self.live <= 0):
            balls.remove(self)

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        X = (obj.x - self.x) ** 2
        Y = (obj.y - self.y) ** 2
        Z = (X + Y) ** 0.5
        if(Z > self.r + obj.r):
            return 0
        else:
           self.live = 0
           return 1
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        return False

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 400
        self.y = 570
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        x0 = pygame.mouse.get_pos()[0]
        y0 = pygame.mouse.get_pos()[1]
        x1 = x0 - self.x
        y1 = self.y - y0
        z = (x1 ** 2 + y1 ** 2) ** 0.5
        k = self.f2_power * 2 / z
        x2 = k * x1
        y2 = k * y1
        pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x + x2, self.y - y2)], 5)
        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

class Target():
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def new_target(self, screen):
        """ Инициализация новой цели. """
        x = self.x = randint(100, 500)
        y = self.y = randint(100, 450)
        r = self.r = randint(2, 50)
        rand_tmp = randint(0, 4)
        if rand_tmp == 0:
             self.vx = 0
             self.vy = 0 
             color = self.color = RED
             self.screen = screen
             self.live = 100
             self.points = 1
        else:
            self.vx = randint(5, 20)
            self.vy = randint(5, 20)
            self.screen = screen
            self.live = 100
            color = self.color = BLACK
            self.points = 1

    def hit(self, points):
        """Попадание шарика в цель."""
        target = Target()
        target.new_target(screen)
        targets.append(target)
        points += self.points
        targets.remove(self)
        return points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        self.live -= 0.01
        if(self.live <= 0):
            targets.remove(self)

    def move(self):
        self.x += self.vx * 0.035
        self.y -= self.vy * 0.035

    def collision(self):
        if(self.x + self.r > 800 or self.x - self.r < 0):
            self.vx *= -1
        if(self.y - self.r < 0 or self.y + self.r > 500):
            self.vy *= -1



def draw_life_screen(points, name, time):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(points), False, BLACK)
    screen.blit(textsurface, (10, 10))


pygame.init()
print('напишите количество целей')
numer_of_targets = int(input())

bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)

for i in range(numer_of_targets):
    target = Target()
    target.new_target(screen)
    targets.append(target)

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for t in targets:
        t.draw()
        t.collision()
        t.move()
    draw_life_screen(POINTS, name, time)
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.collision()
        b.move()
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                POINTS = target.hit(POINTS)
        draw_life_screen(POINTS, name, time)
    gun.power_up()

pygame.quit()
