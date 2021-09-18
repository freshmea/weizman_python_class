# 좌우 방향키를 눌러서 화면이 움직이게 하는 코드를 찾아서 주석을 달아 보세요.
# 캐릭터의 움직임과 화면의 움직임 그리고 UI 의 움직임이 어떻게 되는지 코드를 자세히 살펴 보세요.


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
        self.image = pygame.image.load('../png/tank.png')
        self.image = pygame.transform.scale(self.image, (800, 400))
        self.rect = self.image.get_rect(center=(SCREEN_X/2, SCREEN_Y * 8 / 10))
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(0,0)
        self.health = 100


    def update(self):
        if self.health < 5:
            self.health = 100
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += 10
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x -= 10
        self.rect.centerx = self.pos.x


class Rain(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('skyblue')
        self.red = random.randint(0, 10)
        self.groups = self.game.rains, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((self.bold, self.len))
        self.image.fill(self.color)
        if self.red == 0:
            self.image.fill('Red')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, self.game.sa):
            if self.red == 0 :
                self.game.sa.health -= 10
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
        a = Rain(random.randint(0, SCREEN_X) , 100 , self)
        self.rains.add(a)
        self.all_sprites.add(a)

    def update(self):
        if SCREEN_X/8 > self.sa.pos.x:
            offset_x = -10
            self.sa.pos.x += 10
        elif SCREEN_X*7/8 < self.sa.pos.x:
            offset_x = 10
            self.sa.pos.x -= 10
        else:
            offset_x =0
        for sprite in self.all_sprites:
            sprite.rect.x -= offset_x
        self.all_sprites.update()
        self.ui.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.rains.draw(self.screen)
        self.ui.draw(self.screen)



game = Game()
game.run()
pygame.quit()
