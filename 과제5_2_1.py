# 구름 클래스 추가
# 비가 사선으로 내리기
# 구름 클릭하면 구름 제거 하기
# images 안의 back.png 라는 배경 파일도 같이 있어야 실행이 됩니다.
# images 안의 dino.png 라는 공룡 파일도 같이 있어야 실행이 됩니다.
# images 안의 cloud.svg 라는 구름 파일도 같이 있어야 실행이 됩니다.

import pygame
import random

# 변수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 5


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
        self.game.rains.append(Rain(self.x + random.randint(0, 130), self.y + 70, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect.collidepoint(pos)


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


class Dino:
    def __init__(self, root):
        self.game = root
        self.image = self.game.image_dino
        self.x = SCREEN_X / 2
        self.y = SCREEN_Y - self.image.get_rect().height
        self.speed = 4

    def load_data(self):
        pass

    def move(self):
        self.x += self.speed

    def off_screen(self):
        return self.x < -self.image.get_rect().width or self.x > SCREEN_X

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))


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
        self.dino = Dino(self)

    def load_data(self):
        self.image = pygame.image.load('images/back.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SCREEN_X, SCREEN_Y))
        self.image_dino = pygame.image.load('images/dino.png').convert_alpha()
        self.image_dino = pygame.transform.scale(self.image_dino, (260,200))
        self.image_cloud = pygame.image.load('images/cloud.svg').convert_alpha()

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            # 마우스 버튼이 구름 클릭시 구름 제거
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    if cloud.click():
                        self.clouds.remove(cloud)
                        del cloud

    def update(self):
        # 구름 생성
        while len(self.clouds) < CLOUD_NUMBER:
            self.clouds.append(Cloud(random.randint(0, SCREEN_X), self))
        # 구름에서 비 내리기
        for cloud in self.clouds:
            cloud.rain()
        # 비 움직이게 하고 벗어나면 삭제
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 구름 움직이기
        for cloud in self.clouds:
            cloud.move()
        # 공룡 움직이기
        self.dino.move()
        if self.dino.off_screen():
            self.dino.speed *= -1
            self.dino.image = pygame.transform.flip(self.dino.image, True, False)

    def draw(self):
        self.screen.fill((255, 255, 255))
        # 배경화면
        self.screen.blit(self.image, (0, 0))
        # 비 그리기
        for rain in self.rains:
            rain.draw()
        # 구름 그리기
        for cloud in self.clouds:
            cloud.draw()
        # 공룡 그리기
        self.dino.draw()


game = Game()
game.run()
pygame.quit()
