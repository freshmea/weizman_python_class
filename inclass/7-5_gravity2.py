# # 파이게임 기본(클래스)

import pygame
import random
import cmath

vec = pygame.Vector2
# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60



class Tank(pygame.sprite.Sprite):
    def __init__(self, root, pos, color, layer):
        self.game = root
        self.groups = self.game.all_sprites
        self.image = pygame.image.load('../png/tank.png')
        self.image = pygame.transform.scale(self.image, (600, 300))
        self.pos = pos
        self.dir = vec(random.random(), random.random()).normalize()
        self.speed = 3
        self.rect = self.image.get_rect(topleft=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.mask = pygame.mask.from_surface(self.image)
        self.po = Po(self.game, self.rect.center, color, self._layer - 1, self)
        self.game.all_sprites.add(self.po)

    def update(self):
        # 중력 효과
        self.gravity = 1
        if self.pos.y > SCREEN_Y - 50:
            self.gravity = 0
            self.pos.y = SCREEN_Y - 49
            self.dir = vec(0, 0)
        self.dir.y += self.gravity

        if self.game.pressed_key[pygame.K_LEFT]:
            self.dir.x += -1
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.dir.x += 1
        self.pos += self.dir * self.speed
        self.rect.midbottom = self.pos



class Po(pygame.sprite.Sprite):
    def __init__(self, root, pos, color, layer, tankt):
        self.game = root
        self.tank = tankt
        self.groups = self.game.all_sprites
        self.image_t = pygame.Surface((180, 15))
        self.color = color
        # self.image_t.fill(self.color)
        self.image_t2 = pygame.Surface((180, 15))
        self.image_t2.fill('Black')
        self.image_t.blit(self.image_t2, (-90, 0))
        self.image_t3 = pygame.image.load('../png/po.png').convert_alpha()
        self.image_t3 = pygame.transform.scale(self.image_t3, (90, 15))
        self.image_t.blit(self.image_t3, (90,0))
        self.angle = 0
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        # self.image.set_colorkey((0,0,0))
        self.pos = pos
        self.speed = 3
        self.t_time = 0
        self.rect = self.image.get_rect(center=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update(self):
        self.pos = self.tank.rect.center
        self.rect.center = self.pos
        # # 위아래 키를 눌렀을 때 포가 움직이기
        # if self.game.pressed_key[pygame.K_UP]:
        #     self.angle += 1
        # if self.game.pressed_key[pygame.K_DOWN]:
        #     self.angle -= 1
        # if self.angle > 360:
        #     self.angle -= 360
        # if self.angle < 0:
        #     self.angle += 360
        # 마우스의 좌표로 포가 움직이기
        self.angle = vec(0,0).angle_to(pygame.mouse.get_pos()-self.tank.pos)*-1

        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1).convert_alpha()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(center=self.pos)

    def fire(self, check):
        if check:
            self.t_time = pygame.time.get_ticks()
        if not check:
            self.speed = (pygame.time.get_ticks()-self.t_time)/1000
            print(self.speed)
            a=vec(1,0).rotate(-self.angle)*self.speed
            self.game.all_sprites.add(Ball(self.game, self.pos[0], self.pos[1], a))
            self.game.balls.add(Ball(self.game, self.pos[0], self.pos[1], a))



class Ball(pygame.sprite.Sprite):
    def __init__(self, root, x, y, vel):
        self.size = 5
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, 'Red', (self.size, self.size), self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprites, self.game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(x, y)
        self.vel = vel
        self.mass = 0.006
        self.gravity = vec(0, 0)



    def update(self):
        self.gravi()
        self.vel -= self.gravity
        # self.vel -= (self.pos-vec(SCREEN_X/2, SCREEN_Y/2)).normalize()*(self.pos-vec(SCREEN_X/3*2, SCREEN_Y/2)).length()*(self.pos-vec(SCREEN_X/3*2, SCREEN_Y/2)).length()/100000
        # if self.vel.length()>30:
        #     self.kill()
        #     del self
        #     return
        self.pos += self.vel
        self.rect.center = self.pos
        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_X
        if self.pos.y > SCREEN_Y:
            self.vel.y *= -1
            self.pos.y -= 1
        if self.pos.y < 0:
            self.vel.y *= -1

    def gravi(self):
        self.gravity = vec(0, 0)
        for ball in self.game.all_sprites:
            if not ball == self:
                try:
                    dis = (self.pos - ball.pos).length()
                    dir = (self.pos - ball.pos).normalize()
                    self.gravity += dir * self.mass * ball.mass / (dis * dis)
                except:
                    pass

    def collide(self):
        for other in self.game.balls:
            if not (self == other or other == self.game.bball1):
                if self.rect.colliderect(other):
                    self.size = (self.size*self.size+other.size*other.size)**0.5
                    self.image = pygame.Surface((self.size * 2, self.size * 2))
                    pygame.draw.circle(self.image, 'Red', (self.size, self.size), self.size)
                    self.image.set_colorkey((0, 0, 0))
                    self.rect = self.image.get_rect()
                    self.mass += other.mass
                    self.vel += other.vel
                    other.kill()
                    del other
                    return True

class Bball(pygame.sprite.Sprite):
    def __init__(self, root, x, y, vel):
        self.size = 50
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, 'Blue', (self.size, self.size), self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(x, y)
        self.vel = vel
        self.mass = 1900
        self.gravity = vec(0, 0)

    def update(self):
        self.rect.center = self.pos

    def collide(self):
        pass

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.pressed_key = pygame.key.get_pressed()
        self.bball1 = Bball(self, SCREEN_X/3 , SCREEN_Y/2, vec(0,0))
        #self.bball2 = Bball(self, SCREEN_X/3*2 , SCREEN_Y/2, vec(0,0))
        #self.all_sprites.add(self.bball1, self.bball2)
        self.all_sprites.add(self.bball1)


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
        # if len(self.balls)<1:
        #     a=Ball(self, random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y), vec(-1, 0))
        #     self.all_sprites.add(a)
        #     self.balls.add(a)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tank.po.fire(True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.tank.po.fire(False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    for ball in self.balls:
                        ball.kill()
                        del ball
        # 충돌 체크
        for ball in self.balls:
            if ball.collide():
                break

    def update(self):
        self.pressed_key = pygame.key.get_pressed()
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
