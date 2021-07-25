import pygame
import random

vec = pygame.math.Vector2

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60

class Rect1(pygame.sprite.Sprite):
    def __init__(self, root, pos, color, layer):
        self.game = root
        self.groups = self.game.all_sprites
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.pos = pos
        self.dir = vec(random.random(), random.random()).normalize()
        self.speed = 3
        self.rect = self.image.get_rect(topleft=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update(self):
        self.pos += self.dir*self.speed
        # 무작위로 팅기기
        if self.pos.x > SCREEN_X:
            self.dir = vec(random.random()*-1, random.random()*2-1).normalize()
        if self.pos.y > SCREEN_Y:
            self.dir = vec(random.random()*2-1, random.random()*-1).normalize()
        if self.pos.x < 0:
            self.dir = vec(random.random(), random.random()*2-1).normalize()
        if self.pos.y < 0:
            self.dir = vec(random.random()*2-1, random.random()).normalize()
        # # 중력 효과
        # self.gravity = 1
        # self.dir.y += self.gravity
        # if self.pos.y > SCREEN_Y-100:
        #     self.dir.y = self.dir.y*-1+1

        self.rect.topleft = self.pos

    def re(self, rect):
        if pygame.time.get_ticks()>10000:
            pygame.mixer.Sound.play(self.game.crash)
            self.dir= vec(random.random()*2-1, random.random()*2-1).normalize()
            rect.dir= vec(random.random()*2-1, random.random()*2-1).normalize()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.crash = pygame.mixer.Sound('../wave/2001_key1.mp3')

    def run(self):

        for _ in range(10):
            self.all_sprites.add(Rect1(self, vec(0,0), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 0))
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.draw()
            pygame.display.update()

    def event(self):
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        for rect in self.all_sprites:
            a=pygame.sprite.spritecollide(rect,self.all_sprites, False)
            for aa in a:
                if not aa==rect:
                    aa.re(rect)
        self.all_sprites.update()

    def draw(self):
        self.screen.fill('Black')
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
