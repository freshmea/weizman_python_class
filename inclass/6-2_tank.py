import pygame
import random

vec = pygame.math.Vector2

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60


class Tank(pygame.sprite.Sprite):
    def __init__(self, root, pos, color, layer):
        self.game = root
        self.groups = self.game.all_sprites
        self.image = pygame.Surface((60, 20))
        self.image.fill(color)
        self.pos = pos
        self.dir = vec(random.random(), random.random()).normalize()
        self.speed = 3
        self.rect = self.image.get_rect(topleft=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.po = Po(self.game, self.rect.center, color, self._layer - 1, self)
        self.game.all_sprites.add(self.po)

    def update(self):
        # 중력 효과
        self.gravity = 1
        if self.pos.y > SCREEN_Y - 100:
            self.gravity = 0
            self.pos.y = SCREEN_Y - 99
            self.dir = vec(0, 0)
        self.dir.y += self.gravity

        if self.game.pressed_key[pygame.K_LEFT]:
            self.dir.x += -1
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.dir.x += 1
        self.pos += self.dir * self.speed
        self.rect.topleft = self.pos


class Po(pygame.sprite.Sprite):
    def __init__(self, root, pos, color, layer, tankt):
        self.game = root
        self.tank = tankt
        self.groups = self.game.all_sprites
        self.image_t = pygame.Surface((160, 5))
        self.color = color
        self.image_t.fill(self.color)
        self.image_t2 = pygame.Surface((160, 5))
        self.image_t2.fill('Black')
        self.image_t.blit(self.image_t2, (-80, 0))
        self.angle = 0
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.pos = pos
        self.speed = 3
        self.rect = self.image.get_rect(center=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update(self):
        self.pos = self.tank.rect.center
        self.rect.center = self.pos

        if self.game.pressed_key[pygame.K_UP]:
            self.angle += 1
        if self.game.pressed_key[pygame.K_DOWN]:
            self.angle -= 1
        if self.angle > 360:
            self.angle -= 360
        if self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.rect = self.image.get_rect(center=self.pos)

    def fire(self):
        self.game.all_sprites.add(Bul(self.game, self.pos, self.color, self._layer +1, self.tank, self.angle))


class Bul(pygame.sprite.Sprite):
    def __init__(self, root, pos, color, layer, tankt, angle):
        a=vec(1,0)
        self.game = root
        self.tank = tankt
        self.groups = self.game.all_sprites
        self.image = pygame.Surface((5, 5))
        self.color = color
        self.image.fill(self.color)
        self.angle = angle
        self.pos = pos
        self.vel = a.rotate(self.angle*-1)
        self.speed = 5
        self.gravity = 0.01
        self.rect = self.image.get_rect(center=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update(self):
        self.vel.y += self.gravity
        print(self.vel, self.pos)
        self.pos += self.vel * self.speed
        self.rect.center = self.pos
        if self.pos.y > SCREEN_Y:
            self.kill()
            del self


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('탱크 게임')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.pressed_key = pygame.key.get_pressed()

    def run(self):
        self.tank=Tank(self, vec(0, 0), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
        self.all_sprites.add(self.tank)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tank.po.fire()

    def update(self):
        self.pressed_key = pygame.key.get_pressed()
        self.all_sprites.update()

    def draw(self):
        self.screen.fill('Black')
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()