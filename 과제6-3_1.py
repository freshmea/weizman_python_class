# # 이 게임에 UI 를 추가해서 넣어보세요.
# UI 에 사각형 틀 추가하기
# 체력바를 만들어서 ball의 전체 mass 량을 표현하기
# 글자 넣기

import pygame
import random

vec = pygame.Vector2
# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60


class Ball(pygame.sprite.Sprite):
    def __init__(self, root, x, y, vel, size):
        self.size = size
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, 'Red', (self.size, self.size), self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(x, y)
        self.vel = vel
        self.mass = 10
        self.gravity = vec(0, 0)

    def update(self):
        self.gravi()
        self.vel -= self.gravity
        if self.vel.length() > 30:
            self.devide()
        self.pos += self.vel
        self.rect.center = self.pos
        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_X
        if self.pos.y > SCREEN_Y:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = SCREEN_Y

    def gravi(self):
        self.gravity = vec(0, 0)
        for ball in self.game.all_sprites:
            if not ball == self:
                try:
                    dis = (self.pos - ball.pos).length()
                    direc = (self.pos - ball.pos).normalize()
                    self.gravity += direc * self.mass * ball.mass / (dis * dis)
                except:
                    pass

    def collide(self):
        for other in self.game.all_sprites:
            if not (self == other):
                if self.rect.colliderect(other):
                    self.size = (self.size * self.size + other.size * other.size) ** 0.5
                    self.image = pygame.Surface((self.size * 2, self.size * 2))
                    pygame.draw.circle(self.image, 'Red', (self.size, self.size), self.size)
                    self.image.set_colorkey((0, 0, 0))
                    self.rect = self.image.get_rect()
                    self.mass += other.mass
                    self.vel = (self.vel * self.mass + other.vel * other.mass) / (self.mass + other.mass)
                    other.kill()
                    del other
                    return True

    def devide(self):
        self.vel = self.vel / 2
        self.mass = self.mass /2
        self.size = self.size/(2)**(1/2)
        self.game.all_sprites.add(Ball(self.game, self.pos.x-self.size*2, self.pos.y-self.size*2, self.vel* -1, self.size))

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('흡수하는 볼')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        # 종료 코드
        if len(self.all_sprites) < 16:
            self.all_sprites.add(Ball(self, random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y), vec(-1, 0), 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        for ball in self.all_sprites:
            if ball.collide():
                break

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
