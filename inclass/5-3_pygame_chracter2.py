# 파이게임 비 내리는 코드(클래스)
import pygame
import random
from pygame.locals import *

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 10
RAIN_NUMBER = 5
TITLE = '구름에서 비가 내리는 게임'
CHARACTER_SPEED = 5


class Player:
    def __init__(self, root):
        self.x = 100
        self.y = SCREEN_Y - 200
        self.dx = 0
        self.dy = 0
        self.game = root
        self.image = root.player_image
        self.hit = 0

    def move(self):
        if self.game.pressed_key[K_UP] and self.y > 0:
            self.y += -CHARACTER_SPEED
        if self.game.pressed_key[K_DOWN] and self.y < SCREEN_Y - 200:
            self.y += CHARACTER_SPEED
        if self.game.pressed_key[K_LEFT] and self.x > 0:
            self.x += -CHARACTER_SPEED
        if self.game.pressed_key[K_RIGHT] and self.x < SCREEN_X - 160:
            self.x += CHARACTER_SPEED

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, rain):
        return pygame.Rect(self.x, self.y, 200, 200).collidepoint((rain.x, rain.y))


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('gray')

    def move(self):
        self.y += self.speed
        self.x += 4

    def off_screen(self):
        return self.y > SCREEN_Y

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = random.randint(0, 200)
        self.image = root.image_cloud
        self.game = root
        self.speed = random.randint(3, 10)

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_X:
            self.x = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        for _ in range(RAIN_NUMBER):
            self.game.rains.append(Rain(self.x + random.randint(0, 130), self.y + 70, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect.collidepoint(pos)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.rains = []
        self.clouds = []
        self.player = Player(self)
        self.pressed_key = pygame.key.get_pressed()

    def load_data(self):
        # 배경그림 불러오기
        self.image_background = pygame.image.load('../images/back.png').convert_alpha()
        self.image_background = pygame.transform.scale(self.image_background, (SCREEN_X, SCREEN_Y))
        # 구름그림 불러오기
        self.image_cloud = pygame.image.load('../images/cloud.svg').convert_alpha()
        self.player_image = pygame.image.load('../images/dino.png').convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (260, 200))

    def run(self):
        self.opening()
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
        self.ending()

    def event(self):
        # 종료 코드 및 플레이어 움직임
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            # 마우스 버튼이 구름 클릭시 구름 제거
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    if cloud.click():
                        self.clouds.remove(cloud)
                        del cloud
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.playing = False

    def update(self):
        self.pressed_key = pygame.key.get_pressed()
        # 구름 생성
        while len(self.clouds) < CLOUD_NUMBER:
            self.clouds.append(Cloud(random.randint(1, 20) * SCREEN_X / 20, self))
        # 구름에서 비 생성하고 구름 움직이기
        for cloud in self.clouds:
            cloud.rain()
            cloud.move()
        # 비를 움직이게 하고 화면 밖으로 가면 제거 하기
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 플레이어 움직임
        self.player.move()
        # 플레이어가 비 맞음 체크
        for rain in self.rains:
            if self.player.hit_by(rain):
                self.player.hit += 1
                self.rains.remove(rain)
                del rain

    def draw(self):
        # self.screen.fill((255, 255, 255))
        # 배경화면 그리기
        self.screen.blit(self.image_background, (0, 0))
        # 구름 그리기
        for cloud in self.clouds:
            cloud.draw()
        # 비 그리기
        for rain in self.rains:
            rain.draw()
        # 플레이어 그리기
        self.player.draw()

    def opening(self):
        self.screen.fill(pygame.Color('black'))
        stop = True
        self.draw_text(f'스페이스 바를 누르면 게임이 시작 됩니다.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 1 / 20)
        self.draw_text(f'구름을 클릭하면 구름이 사라집니다.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 2 / 20)
        self.draw_text(f'방향키로 공룡을 조작합니다.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 34 / 20)
        self.draw_text(f'q를 누르면 게임이 끝납니다.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 3 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def ending(self):
        self.screen.fill(pygame.Color('black'))
        stop = True
        self.draw_text(f'스페이스 바를 누르면 게임이 종료됩니다.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 1 / 20)
        self.draw_text(f'게임을 플레이해 주셔서 감사합니다.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 2 / 20)
        self.draw_text(f'^^', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 3 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)


game = Game()
game.run()
pygame.quit()
