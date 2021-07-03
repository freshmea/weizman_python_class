# # 파이게임 기본 코드
# import pygame
#
# pygame.init()
# pygame.display.set_caption('게임 제목')
# Screen_x = 640 * 2 # 화면 넓이
# Screen_y = 480 * 2 # 화면 높이
# screen = pygame.display.set_mode((Screen_x, Screen_y)) # 화면 세팅
# clock = pygame.time.Clock() # 시계 지정
#
# playing = True
#
#
# while playing:
#     clock.tick(60)
#     """종료시 프로그램 종료시키는 코드"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             playing = False
#     pygame.display.update()
#
# pygame.quit()


# #파이게임 기본 코드(클래스)
# import pygame
#
# Screen_x = 640 * 2  # 화면 넓이
# Screen_y = 480 * 2  # 화면 높이
#
# class Game:
#     def __init__(self):
#         pygame.init()
#         pygame.display.set_caption('게임 제목')
#         self.screen = pygame.display.set_mode((Screen_x, Screen_y)) # 화면 세팅
#         self.clock = pygame.time.Clock() # 시계 지정
#         self.playing = True
#     def run(self):
#         while self.playing:
#             self.clock.tick(60)
#             self.event()
#             pygame.display.update()
#
#     def event(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.playing = False
#
# game = Game()
# game.run()
# pygame.quit()


# 파이게임 비 내리는 코드(클래스)
import pygame
import random

# 변수
Screen_x = 640 * 2  # 화면 넓이
Screen_y = 480 * 2  # 화면 높이
FPS = 60


class Rain:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = game
        self.len = random.randint(5, 15)
        self.color = (125, 255, 255)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > Screen_y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.rains = []
        self.load_data()

    def load_data(self):
        self.image = pygame.image.load('../images/back.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (Screen_x, Screen_y))

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
        for i in range(10):
            self.rains.append(Rain(random.randint(0, Screen_x), 0, self))
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image, (0, 0))
        for rain in self.rains:
            rain.draw()


game = Game()
game.run()
pygame.quit()
