import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
vec = pygame.math.Vector2


def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont('malgungothic', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    surface.blit(text_surface, text_rect)

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
        pygame.draw.rect(self.image, 'Gray', (10, 10, SCREEN_X - 20, SCREEN_Y - 20), 10, 10)
        self.ui_health = self.game.sa.health
        pygame.draw.line(self.image, 'Red', (100, SCREEN_Y - 100), (100 + self.ui_health * 3, SCREEN_Y - 100), 15)
        draw_text(self.image, f'체력: {self.ui_health}', 30, pygame.Color('Red'), 100, SCREEN_Y - 100)



class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.image.load('../png/tank.png')
        self.image = pygame.transform.scale(self.image, (800, 400))
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(SCREEN_X / 2, SCREEN_Y * 8 / 10)
        self.health = 100

    def update(self):
        if self.health < 5:
            self.health = 100
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += 10
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x -= 10
        self.rect.center = self.pos


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
        self.pos = vec(x, y)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, self.game.sa):
            if self.red == 0:
                self.game.sa.health -= 10
                self.game.hit_sound.play()
            self.kill()
            del self
            return
        self.pos.y += self.speed
        self.rect.topleft = self.pos
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
        self.bg = pygame.image.load('../png/BG/BG.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_X, SCREEN_Y))
        self.camera = vec(0, 0)
        self.bgcamera = vec(0, 0)
        pygame.mixer.music.load('../wave/bgmusic.wav')
        pygame.mixer.music.set_volume(0.4)
        self.hit_sound = pygame.mixer.Sound('../wave/explosion2.wav')

    def run(self):
        pygame.mixer.music.play(-1)
        self.opening()
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
        self.ending()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        a = Rain(random.randint(0, SCREEN_X), 100, self)
        self.rains.add(a)
        self.all_sprites.add(a)

    def update(self):
        if SCREEN_X / 8 * 2 > self.sa.pos.x:
            self.camera.x = -10
        elif SCREEN_X * 6 / 8 < self.sa.pos.x:
            self.camera.x = 10
        else:
            self.camera.x = 0
        for sprite in self.all_sprites:
            sprite.pos.x -= self.camera.x
        self.bgcamera += self.camera
        self.all_sprites.update()
        self.ui.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        for n in range(5):
            self.screen.blit(self.bg, (SCREEN_X * (n - 2) - self.bgcamera.x, 0))
        self.all_sprites.draw(self.screen)
        self.rains.draw(self.screen)
        self.ui.draw(self.screen)

    def opening(self):
        self.screen.blit(self.bg, (0, 0))
        stop = True
        draw_text(self.screen, f'스페이스 바를 누르면 게임이 시작 됩니다.', 30, pygame.Color('red'), 100, SCREEN_Y * 1 / 20)
        draw_text(self.screen, f'구름을 클릭하면 구름이 사라집니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 2 / 20)
        draw_text(self.screen, f'방향키로 공룡을 조작합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 3 / 20)
        draw_text(self.screen, f'스페이스바를 누르면 점프 합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 4 / 20)
        draw_text(self.screen, f'붉은 비를 많이 모으면 게임을 클리어 합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 5 / 20)
        draw_text(self.screen, f'버섯을 먹으면 속도와 크기가 커집니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 6 / 20)
        draw_text(self.screen, f'q를 누르면 게임이 끝납니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 7 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[pygame.K_SPACE]:
                stop = False
            # 종료 코드
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = False
                    self.playing = False

    def ending(self):
        self.screen.blit(self.bg, (0, 0))
        stop = True
        draw_text(self.screen, f'q를 누르면 게임이 종료됩니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 2 / 20)
        draw_text(self.screen, f'게임을 플레이해 주셔서 감사합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 3 / 20)
        draw_text(self.screen, f'^^', 30, pygame.Color('black'), 100, SCREEN_Y * 4 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[pygame.K_q]:
                stop = False
            # 종료 코드
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = False

game = Game()
game.run()
pygame.quit()
