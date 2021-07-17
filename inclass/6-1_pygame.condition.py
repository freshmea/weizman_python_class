# 파이게임 비 내리는 코드(클래스)
import pygame
import random
from pygame.locals import *

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 10
RAIN_NUMBER = 1
TITLE = '구름에서 비가 내리는 게임'


class Player(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        pygame.sprite.Sprite.__init__(self)
        self.image = root.player_images_idle_r[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = SCREEN_Y - 200
        self.hit = 0
        self.index = 0
        self.now = 0
        self.walking_r = False
        self.walking_l = False
        self.jumping = False
        self.jumpa = 0
        self.images = self.game.player_images_walk_r
        self.mask = pygame.mask.from_surface(self.image)
        self.layer = 1
        self.booster = 0
        self.character_speed = 5

    def update(self):
        self.animation()
        self.move()
        if self.booster == 1:
            self.character_speed = 10

    def animation(self):
        if self.jumping:
            if self.images == game.player_images_walk_r or self.images == game.player_images_idle_r or self.images == game.player_images_jump_r:
                self.images = game.player_images_jump_r
            else:
                self.images = game.player_images_jump_l
        elif self.walking_r:
            self.images = game.player_images_walk_r
        elif self.walking_l:
            self.images = game.player_images_walk_l
        else:
            if self.images == game.player_images_walk_r or self.images == game.player_images_idle_r or self.images == game.player_images_jump_r:
                self.images = game.player_images_idle_r
            else:
                self.images = game.player_images_idle_l

        self.image = self.images[self.index]
        if pygame.time.get_ticks() - self.now > 100:
            self.now = pygame.time.get_ticks()
            self.index += 1
        if self.index > len(self.images) - 1:
            self.index = 0
        if self.booster == 1:
            self.image = pygame.transform.scale2x(self.image)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        # # 위 아래로 움직이기
        # if self.game.pressed_key[K_UP] and self.rect.y > 0:
        #     self.rect.y += -CHARACTER_SPEED
        # if self.game.pressed_key[K_DOWN] and self.rect.y < SCREEN_Y - 200:
        #     self.rect.y += CHARACTER_SPEED
        if self.game.pressed_key[K_LEFT] and self.rect.centerx > 0:
            self.rect.centerx += -self.character_speed
            self.walking_l = True
        else:
            self.walking_l = False
        if self.game.pressed_key[K_RIGHT] and self.rect.centerx < SCREEN_X - 160:
            self.rect.centerx += self.character_speed
            self.walking_r = True
        else:
            self.walking_r = False
        if self.game.pressed_key[K_SPACE]:
            self.jumping = True
            self.index = 0
        if self.jumping:
            self.jump()

    def jump(self):
        if self.jumpa < 100:
            self.jumpa += 1
        else:
            self.jumpa = 0
            self.jumping = False
            self.index = 0
        if self.jumpa < 50:
            self.rect.centery -= self.character_speed
        else:
            self.rect.centery += self.character_speed
        if self.rect.centery > SCREEN_Y - 200:
            self.jumpa = 0
            self.jumping = False
            self.index = 0
            self.rect.centery = SCREEN_Y - 200
            if self.booster == 1:
                self.rect.centery -= 200

    def hit_by(self, rain):
        return pygame.sprite.collide_mask(self, rain)


class Rain(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.game = root
        self.groups = self.game.all_sprites, self.game.rains
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.len = random.randint(5, 15)
        self.bold = random.randint(1, 4)
        self.color = pygame.Color('red')
        self.image = pygame.Surface((self.bold, self.len))
        self.rect = self.image.get_rect()
        self.image.fill(color=self.color)
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = random.randint(5, 28)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.move()
        if self.game.player.hit_by(self):
            self.game.player.hit += 1
            self.kill()
            del self
            return
        if self.off_screen():
            self.kill()
            del self

    def move(self):
        self.rect.centery += self.speed
        self.rect.centerx += 4

    def off_screen(self):
        return self.rect.centery > SCREEN_Y


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, root):
        self.game = root
        self.groups = self.game.all_sprites, self.game.clouds
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = root.image_cloud
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(0, 200)
        self.speed = random.randint(3, 10)

    def update(self):
        self.move()
        self.rain()

    def move(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_X:
            self.rect.x = 0

    def rain(self):
        for _ in range(RAIN_NUMBER):
            self.game.all_sprites.add(Rain(self.rect.x + random.randint(0, 130), self.rect.y + 70, self.game))
            self.game.rains.add(Rain(self.rect.x + random.randint(0, 130), self.rect.y + 70, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        return rect.collidepoint(pos)


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.game = root
        self.groups = self.game.all_sprites, self.game.birds
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.images = self.game.birds_images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = random.randint(3, 20)
        self.index = 0
        self.now = 0

    def update(self):
        self.animate()
        self.move()

    def animate(self):
        if pygame.time.get_ticks() - self.now > 100:
            self.now = pygame.time.get_ticks()
            self.image = self.game.birds_images[self.index]
            self.index += 1
        if self.index > len(self.images) - 1:
            self.index = 0

    def move(self):
        self.rect.centerx += self.speed
        self.rect.centery -= int(self.speed / random.randint(1, 5))
        if self.rect.centerx > SCREEN_X:
            self.kill()
            del self


class Booster(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.game = root
        self.groups = self.game.all_sprites, self.game.boosters
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.booster_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.index = 0
        self.now = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.hit_by():
            self.game.player.booster = random.randint(1,1)
            self.kill()
        self.move()

    def move(self):
        self.rect.centerx += 1
        if self.rect.centerx > SCREEN_X:
            self.rect.centerx = 0

    def hit_by(self):
        return pygame.sprite.collide_mask(self, self.game.player)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.clouds = pygame.sprite.Group()
        self.birds = pygame.sprite.Group()
        self.rains = pygame.sprite.Group()
        self.boosters = pygame.sprite.Group()
        self.player = Player(self)
        self.pressed_key = pygame.key.get_pressed()
        self.clear = False


    def load_data(self):
        # 배경그림 불러오기
        self.image_background = pygame.image.load('../png/BG/BG.png').convert_alpha()
        self.image_background2 = pygame.image.load('../png/storyboard6.png').convert_alpha()
        self.image_background = pygame.transform.scale(self.image_background, (SCREEN_X, SCREEN_Y))
        self.image_background2 = pygame.transform.scale(self.image_background2, (SCREEN_X, SCREEN_Y))
        # 구름 이미지 불러오기
        self.image_cloud = pygame.image.load('../images/cloud.svg').convert_alpha()
        # 플레이어 이미지 불러오기
        self.player_images_idle_r = [pygame.image.load(f'../png/Idle ({x}).png').convert_alpha() for x in range(1, 11)]
        self.player_images_idle_l = []
        self.player_images_jump_r = [pygame.image.load(f'../png/Jump ({x}).png').convert_alpha() for x in range(1, 13)]
        self.player_images_jump_l = []
        self.player_images_walk_r = [pygame.image.load(f'../png/Walk ({x}).png').convert_alpha() for x in range(1, 11)]
        self.player_images_walk_l = []
        for image in self.player_images_idle_r:
            self.player_images_idle_r[self.player_images_idle_r.index(image)] = pygame.transform.scale(image,
                                                                                                       (260, 200))
        for image in self.player_images_idle_r:
            self.player_images_idle_l.append(pygame.transform.flip(image, True, False))
        for image in self.player_images_jump_r:
            self.player_images_jump_r[self.player_images_jump_r.index(image)] = pygame.transform.scale(image,
                                                                                                       (260, 200))
        for image in self.player_images_jump_r:
            self.player_images_jump_l.append(pygame.transform.flip(image, True, False))
        for image in self.player_images_walk_r:
            self.player_images_walk_r[self.player_images_walk_r.index(image)] = pygame.transform.scale(image,
                                                                                                       (260, 200))
        for image in self.player_images_walk_r:
            self.player_images_walk_l.append(pygame.transform.flip(image, True, False))
        # 새 이미지 불러오기
        self.birds_images = [pygame.image.load(f'../png/bird ({x}).png').convert_alpha() for x in range(1, 6)]
        for image in self.birds_images:
            self.birds_images[self.birds_images.index(image)] = pygame.transform.scale(image, (100, 50))
        # 부스터 이미지 불러오기
        self.booster_image = pygame.image.load(f'../png/Object/Mushroom_1.png').convert_alpha()

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
            #마우스 버튼이 구름 클릭시 구름 제거
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    if cloud.click():
                        cloud.kill()
                        del cloud
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.playing = False
        # 종료 이벤트
        if self.player.hit > 5000:
            self.playing = False
            self.clear = True
        if pygame.time.get_ticks() > 30000:
            self.playing = False

    def update(self):
        self.pressed_key = pygame.key.get_pressed()
        while len(self.clouds) < CLOUD_NUMBER:
            self.clouds.add(Cloud(random.randint(1, 20) * SCREEN_X / 20, self))
            self.all_sprites.add(Cloud(random.randint(1, 20) * SCREEN_X / 20, self))
        while len(self.birds.sprites()) < CLOUD_NUMBER:
            self.birds.add(Bird(0, random.randint(1, 20) * SCREEN_Y / 20, self))
            self.all_sprites.add(Bird(0, random.randint(1, 20) * SCREEN_Y / 20, self))
        while len(self.boosters.sprites()) < 2:
            self.boosters.add(Booster(random.randint(1, 20) * SCREEN_X / 20, random.randint(1, 20)*20+SCREEN_Y-600, self))
            self.all_sprites.add(Booster(random.randint(1, 20) * SCREEN_X / 20, random.randint(1, 20)*20 + SCREEN_Y-600, self))
        if not self.all_sprites.has(self.player):
            self.all_sprites.add(self.player, layer=self.player.layer)
        self.all_sprites.update()

    def draw(self):
        # 배경화면 그리기
        self.screen.blit(self.image_background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text(f'비가 내리고 있습니다. {self.player.hit}/5000 플레이 타임 {pygame.time.get_ticks()/1000}/30 캐릭터 스피드 {self.player.character_speed}', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 1 / 20)

    def opening(self):
        self.screen.blit(self.image_background2, (0,0))
        stop = True
        self.draw_text(f'스페이스 바를 누르면 게임이 시작 됩니다.', 30, pygame.Color('red'), 100, SCREEN_Y * 1 / 20)
        self.draw_text(f'구름을 클릭하면 구름이 사라집니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 2 / 20)
        self.draw_text(f'방향키로 공룡을 조작합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 3 / 20)
        self.draw_text(f'스페이스바를 누르면 점프 합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 4 / 20)
        self.draw_text(f'붉은 비를 많이 모으면 게임을 클리어 합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 5 / 20)
        self.draw_text(f'버섯을 먹으면 속도와 크기가 커집니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 6 / 20)
        self.draw_text(f'q를 누르면 게임이 끝납니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 7 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def ending(self):
        self.screen.blit(self.image_background2, (0,0))
        stop = True
        if self.clear == True:
            self.draw_text(f'축하합니다. 붉은비를 충분히 모았습니다. 게임 클리어!!', 30, pygame.Color('red'), 100, SCREEN_Y * 1 / 20)
        else:
            self.draw_text(f'붉은 비를 많이 못 얻었네요.... ㅠㅠ ', 30, pygame.Color('red'), 100, SCREEN_Y * 1 / 20)
        self.draw_text(f'q를 누르면 게임이 종료됩니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 2 / 20)
        self.draw_text(f'게임을 플레이해 주셔서 감사합니다.', 30, pygame.Color('black'), 100, SCREEN_Y * 3 / 20)
        self.draw_text(f'^^', 30, pygame.Color('black'), 100, SCREEN_Y * 4 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_q]:
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
