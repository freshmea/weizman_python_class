# # 파이게임 기본(클래스)

import pygame
import random

vec = pygame.Vector2
# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60


class Ball(pygame.sprite.Sprite):
    def __init__(self, root, x, y, vel):
        self.size = 10
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, 'Red', (self.size, self.size), self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(x, y)
        # self.vel = vec(0,random.randint(10,20))
        self.vel = vel
        self.mass = 100
        self.gravity = vec(0, 0)

    def update(self):
        self.gravi()
        self.vel -= self.gravity
        # self.vel -= (self.pos-vec(SCREEN_X/2, SCREEN_Y/2)).normalize()*(self.pos-vec(SCREEN_X/3*2, SCREEN_Y/2)).length()*(self.pos-vec(SCREEN_X/3*2, SCREEN_Y/2)).length()/100000
        if self.vel.length()>10:
            self.vel = self.vel /2
        self.pos += self.vel
        self.rect.center = self.pos
        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_X
        if self.pos.y > SCREEN_Y:
            self.vel.y *= -1
            self.pos.y -= 1
        if self.pos.y < 0:
            self.vel.y *= -1

    def gravi(self):
        self.gravity = vec(0, 0)
        for ball in self.game.all_sprites:
            if not ball == self:
                try:
                    dis = (self.pos - ball.pos).length()
                    dir = (self.pos - ball.pos).normalize()
                    self.gravity += dir * self.mass / (dis * dis)
                except:
                    pass


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
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
        if len(self.all_sprites) < 100:
            self.all_sprites.add(Ball(self, random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y), vec(-1, 0)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        for ball in self.all_sprites:
            for other in self.all_sprites:
                ball.rect.colliderect(other)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        # pygame.draw.circle(self.screen, 'White', (SCREEN_X/3, SCREEN_Y/2), 10)
        # pygame.draw.circle(self.screen, 'White', (SCREEN_X/3*2, SCREEN_Y/2), 10)
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
