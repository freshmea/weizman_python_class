# 오늘 만든 코드에서 사각형을 직사각형으로 만들고 회전을 시키기
# x 좌표가 화면을 넘어가면 0으로 만들기
# 부딧히면 반대 방향으로 팅기기
# 많이 부딪히면 사라지게 하기
# 색깔과 직사각형 모양 랜덤으로 만들기
# 볼륨 줄이기
# 스페이스 바를 놓았을 때 랜덤 으로 방향 설정
# 사각형 객체가 20개 이하가 되면 다시 생성
# 배경화면 추가해서 화면에 맞추어서 늘리기

# 각각을 지정한 코드에 주석을 달아서 코드를 완성하세요.
# 스페이스바를 연속으로 눌러 보세요.

import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
GRAVITY = 0.3


class Figure(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.Surface((random.randint(5, 10), random.randint(5, 10)))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = pygame.Vector2(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y))
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
        self.speed = 2
        self.rotate = 0
        self.rotate_speed = random.randint(1, 3)
        self.col_lim = random.randint(0, 5) * -1

    def update(self):
        self.rotate += self.rotate_speed
        self.image = pygame.transform.rotozoom(self.image_t, self.rotate, 1)
        self.image.set_colorkey((0, 0, 0))
        if self.game.pressed_key[pygame.K_SPACE]:
            self.dir.y += GRAVITY
            self.pos += self.dir * self.speed
            if self.pos.y > SCREEN_Y:
                self.pos.y = SCREEN_Y - 10

            self.rect.center = self.pos
        else:
            if self.pos.x > SCREEN_X:
                self.pos.x = 0
            if self.pos.x < 0:
                self.pos.x = SCREEN_X
            if self.pos.y > SCREEN_Y:
                self.pos.y = 0
            if self.pos.y < 0:
                self.pos.y = SCREEN_Y
            self.dir = self.dir.normalize()
            self.pos += self.dir * self.speed
            self.rect.center = self.pos

        if self.col_lim > 3:
            self.kill()
            del self

    def col(self):
        self.dir = self.dir * -1
        self.col_lim += 1

    def reset(self):
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('사각형 게임 ')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.bomb = pygame.mixer.Sound('../wave/2001_key1.mp3')
        self.bomb.set_volume(0.1)
        self.back = pygame.image.load('../images/starfalling.jpg')
        self.back = pygame.transform.scale(self.back, (SCREEN_X, SCREEN_Y))

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                for a in self.all_sprites:
                    a.reset()
        for figure in self.all_sprites:
            re = pygame.sprite.spritecollide(figure, self.all_sprites, False)
            for a in re:
                if not figure == a:
                    pygame.mixer.Sound.play(self.bomb)
                    figure.col()

    def update(self):
        if len(self.all_sprites) < 20:
            self.all_sprites.add(Figure(self))
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.back, (0, 0))
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
