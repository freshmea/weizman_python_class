# # 파이게임 기본(클래스)

import pygame, random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
GRAVITY = 0.3

class Figure(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.Surface((30, 30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = pygame.Vector2(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y))
        self.dir = pygame.Vector2(random.random()*2-1, random.random()*2-1)
        self.speed = 2

    def update(self):
        if self.game.pressed_key[pygame.K_SPACE]:
            self.dir.y += GRAVITY
            self.pos += self.dir * self.speed
            if self.pos.y > SCREEN_Y:
                self.pos.y = SCREEN_Y-10
            self.rect.center = self.pos
        else:
            if self.pos.x >SCREEN_X:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            if self.pos.x < 0 :
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            if self.pos.y > SCREEN_Y:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            if self.pos.y < 0:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            self.dir = self.dir.normalize()
            self.pos += self.dir * self.speed
            self.rect.center = self.pos

    def col(self):
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        for _ in range(10):
            self.all_sprites.add(Figure(self))
        self.bomb =pygame.mixer.Sound('wave/2001_key1.mp3')


    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        for figure in self.all_sprites:
            re = pygame.sprite.spritecollide(figure, self.all_sprites, False)
            for a in re:
                if not figure == a:
                    pygame.mixer.Sound.play(self.bomb)
                    figure.col()
                    a.col()


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
