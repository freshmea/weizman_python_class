import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60

class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.image.load('../png/tank.png')
        self.image = pygame.transform.scale(self.image, (800, 400))
        self.rect = self.image.get_rect(center=(SCREEN_X/2, SCREEN_Y * 8 / 10))
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(0,0)

    def update(self):
        self.pos.x += 8
        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        self.rect.centerx = self.pos.x



class Rain(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('skyblue')
        self.red = random.randint(0, 100)
        self.groups = self.game.rains
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((self.bold, self.len))
        self.image.fill(self.color)
        if self.red == 0:
            self.image.fill('Red')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, self.game.sa):
            self.kill()
            del self
            return
        self.rect.y += self.speed
        if self.off_screen():
            self.kill()
            del self
            return

    def off_screen(self):
        return self.rect.y > SCREEN_Y + 20


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.sa = Sa(self)
        self.rains = pygame.sprite.Group()

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
        self.rains.add(Rain(random.randint(0, SCREEN_X) , 100 , self))

    def update(self):
        self.all_sprites.update()
        self.rains.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.rains.draw(self.screen)



game = Game()
game.run()
pygame.quit()
