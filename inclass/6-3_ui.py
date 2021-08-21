import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60


class Ui(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.groups = self.game.ui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((SCREEN_X, SCREEN_Y))
        self.rect = self.image.get_rect()
        self.image.set_colorkey('Black')
        self.ui_health = self.game.sa.health

    def update(self):
        self.image.fill('Black')
        pygame.draw.rect(self.image, 'Gray', (10,10, SCREEN_X-20, SCREEN_Y-20), 10, 10)
        self.ui_health = self.game.sa.health
        pygame.draw.line(self.image, 'Red', (100, SCREEN_Y-100), (100+self.ui_health*3, SCREEN_Y-100), 15)
        self.draw_text(f'체력: {self.ui_health}', 30, pygame.Color('Red'), 100, SCREEN_Y -100)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_surface, text_rect)

class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        #self.image = pygame.Surface((200, 50))
        self.image = pygame.image.load('../png/tank.png')
        self.image = pygame.transform.scale(self.image, (800, 400))
        #self.image.fill('Red')
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.centerx = SCREEN_X/2
        self.rect.centery = SCREEN_Y * 8 / 10
        self.angle = 0
        self.mask = self.image.get_masks()
        self.pos = pygame.math.Vector2(0,0)
        self.health = 100

    def update(self):
        #self.angle += 1
        self.health -= 1
        if self.health < 5:
            self.health = 100
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
        self.ui = pygame.sprite.GroupSingle()
        self.ui.add(Ui(self))

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        self.pressed_key =pygame.key.get_pressed()
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
        self.ui.update()
        for sprite in self.all_sprites:
            if self.pressed_key[pygame.K_RIGHT]:
                sprite.pos.x -= 1
            if self.pressed_key[pygame.K_LEFT]:
                sprite.pos.x += 1

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        for rain in self.rains:
            rain.draw()
        self.ui.draw(self.screen)



game = Game()
game.run()
pygame.quit()
