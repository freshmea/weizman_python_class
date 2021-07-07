# 움직이는 공룡 클래스 추카
# images 안의 back.png 라는 배경 파일도 같이 있어야 실행이 됩니다.
# images 안의 dino.png 라는 공룡 파일도 같이 있어야 실행이 됩니다.

# 비 오는 날의 공룡
import pygame
import random

# 변수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.root = root
        self.len = random.randint(5, 15)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > SCREEN_Y - 200

    def draw(self):
        pygame.draw.line(self.root.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Dino:
    def __init__(self, root):
        self.root = root
        self.image = self.root.image_dino
        self.x = SCREEN_X / 2
        self.y = SCREEN_Y - 600
        self.speed = 4

    def load_data(self):
        pass

    def move(self):
        self.x += self.speed

    def off_screen(self):
        return self.x < -600 or self.x > SCREEN_X - 100

    def draw(self):
        self.root.screen.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.rains = []
        self.dino = Dino(self)

    def load_data(self):
        self.image = pygame.image.load('images/back.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SCREEN_X, SCREEN_Y))
        self.image_dino = pygame.image.load('images/dino.png').convert_alpha()

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

    def update(self):
        for i in range(3):
            self.rains.append(Rain(random.randint(0, SCREEN_X), 0, self))
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        self.dino.move()
        if self.dino.off_screen():
            self.dino.speed *= -1
            self.dino.image=pygame.transform.flip(self.dino.image, True, False)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image, (0, 0))
        for rain in self.rains:
            rain.draw()
        self.dino.draw()



game = Game()
game.run()
pygame.quit()