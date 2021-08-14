import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60

class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.images = [pygame.image.load('../png/Idle (1).png'),
                       pygame.image.load('../png/Idle (2).png'),
                       pygame.image.load('../png/Idle (3).png'),
                       pygame.image.load('../png/Idle (4).png'),
                       pygame.image.load('../png/Idle (5).png'),
                       pygame.image.load('../png/Idle (6).png'),
                       pygame.image.load('../png/Idle (7).png'),
                       pygame.image.load('../png/Idle (8).png'),
                       pygame.image.load('../png/Idle (9).png'),
                       pygame.image.load('../png/Idle (10).png')
                       ]
        self.index = 0

        self.image = pygame.transform.scale(self.image, (800, 400))
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.centerx = SCREEN_X/2
        self.rect.centery = SCREEN_Y * 8 / 10
        self.angle = 0
        self.mask = self.image.get_masks()
        self.pos = pygame.math.Vector2(0,0)

    def update(self):
        #self.angle += 1
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.pos.x += 8
        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        self.pos.y = SCREEN_Y * 8 / 10
        self.rect.center = self.pos


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('skyblue')
        self.red = random.randint(0, 100)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > SCREEN_Y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)
        if self.red == 0:
            pygame.draw.line(self.game.screen, pygame.Color('red'), (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.sa = Sa(self)
        self.rains = []

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        self.rains.append(Rain(random.randint(0, SCREEN_X) , 100 , self))

    def update(self):
        self.all_sprites.update()
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        for rain in self.rains:
            rain.draw()



game = Game()
game.run()
pygame.quit()
