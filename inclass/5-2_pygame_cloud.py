# 파이게임 비 내리는 코드(클래스)
import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 5
RAIN_NUMBER = 1


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = (125, 255, 255)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > SCREEN_Y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = 50
        self.game = root
        self.image = root.cloud_image

    def move(self):
        if self.x >= SCREEN_X:
            self.x = 1
        self.x += 3

    def rain(self):
        for _ in range(RAIN_NUMBER):
            self.game.rains.append(Rain(random.randint(self.x, self.x + 130), self.y + 70, self.game))

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.rains = []
        self.clouds = []

    def load_data(self):
        # 배경그림 불러오기
        self.image_background = pygame.image.load('../images/back.png').convert_alpha()
        self.image_background = pygame.transform.scale(self.image_background, (SCREEN_X, SCREEN_Y))
        # 구름그림 불러오기
        self.cloud_image = pygame.image.load('../images/cloud.svg').convert_alpha()

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

    def update(self):
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

    def draw(self):
        self.screen.fill((255, 255, 255))
        # 배경화면 그리기
        self.screen.blit(self.image_background, (0, 0))
        # 구름 그리기
        for cloud in self.clouds:
            cloud.draw()
        # 비 그리기
        for rain in self.rains:
            rain.draw()


game = Game()
game.run()
pygame.quit()
