
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
# class Game:
#     def __init__(self):
#         pygame.init()
#         pygame.display.set_caption('게임 제목')
#         Screen_x = 640 * 2 # 화면 넓이
#         Screen_y = 480 * 2 # 화면 높이
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


class Rain:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
        self.bold = random.randint(1, 4)
        self.game = game

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > Screen_y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.rains = []

    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.rains.append(Rain(random.randint(10, Screen_x-10), 10, self))
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain

    def draw(self):
        self.screen.fill((255, 255, 255))
        for rain in self.rains:
            rain.draw()


game = Game()
game.run()
pygame.quit()