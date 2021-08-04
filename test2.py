# 파이게임 기본 코드
import pygame
import random


def rotcenter(image, angle):
    return pygame.transform.rotate(image, angle)


pygame.init()
pygame.display.set_caption('게임 제목')
Screen_x = 640 * 2  # 화면 넓이
Screen_y = 480 * 2  # 화면 높이
GRAVITY = 0.3
screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
clock = pygame.time.Clock()  # 시계 지정

playing = True


class Figure(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.Surface((20, 70))
        self.image.fill((255, 0, 0))
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = pygame.Vector2(random.randint(0, Screen_x), random.randint(0, Screen_y))
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
        self.speed = 10
        self.rotate = 0

    def update(self):
        self.rotate += 1
        self.image = pygame.transform.rotozoom(self.image_t, self.rotate, 1)
        rotcenter(self.image, 90)
        if self.game.pressed_key[pygame.K_SPACE]:

            self.dir.y += GRAVITY
            self.pos += self.dir * self.speed
            if self.pos.y > Screen_y:
                self.pos.y = Screen_y - 150
            self.rect.center = self.pos

        else:

            self.pos += self.dir * self.speed
            if self.pos.x > Screen_x:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            if self.pos.x < 0:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            if self.pos.y > Screen_y:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            if self.pos.y < 0:
                self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
            self.dir = self.dir.normalize()
            self.rect.center = self.pos

    def col(self):
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)


# 파이게임 기본 코드(클래스)


Screen_x = 640 * 2  # 화면 넓이
Screen_y = 480 * 2  # 화면 높이


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('화면 보호기(?)')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True

        self.all_sprites = pygame.sprite.Group()
        self.figure = Figure(self)
        for i in range(20):
            self.all_sprites.add(Figure(self))

#        self.bomb = pygame.mixer.Sound('18.wav')

    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        for figure in self.all_sprites:
            re = pygame.sprite.spritecollide(figure, self.all_sprites, False)
            for a in re:
                if not figure == a:
#                    pygame.mixer.Sound.play(self.bomb)
                    pass

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()