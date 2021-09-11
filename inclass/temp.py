# 파이게임 기본(클래스)

import pygame, random

# 전역상수
SCREEN_X = 640  # 화면 넓이
SCREEN_Y = 480  # 화면 높이
FPS = 60
vec = pygame.math.Vector2


def draw_text(self, text, size, color, x, y):
    font = pygame.font.SysFont('malgungothic', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    self.screen.blit(text_surface, text_rect)


class Mogi(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('../png/bird (1).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.mogi
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.center = (100, 30)
        self.pos = vec(random.randint(0, SCREEN_X), 50)
        self.dir = vec(0, 0)
        self.time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
        self.v_bool = True

    def update(self):
        self.dir = vec(random.random() * random.randint(-20, 20), random.random() * random.randint(-20, 20))
        if pygame.time.get_ticks() - self.time < 2000:
            self.time = pygame.time.get_ticks()
            self.pos += self.dir
            self.rect.center = self.pos
        if self.pos.x < 0 or self.pos.x > SCREEN_X:
            self.kill()
            del self
            return
        self.event()

    def event(self):
        if pygame.sprite.collide_mask(self, self.game.stick) and pygame.mouse.get_pressed(3)[0] and self.v_bool:
            print(f'잡음{random.randint(1,100)}')

            self.kill()
            del self
            return
        if pygame.mouse.get_pressed(3)[0] == True:
            self.v_bool = False

        else:
            self.v_bool = True


class Mogistick(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('../png/bird (1).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.mogichea
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.center = (100, 30)
        self.pos = vec(random.randint(0, SCREEN_X), 50)
        self.dir = vec(0, 0)
        self.time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.rect.bottomright = self.pos - vec(-22, -23)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprite = pygame.sprite.Group()
        self.mogi = pygame.sprite.Group()
        self.mogichea = pygame.sprite.Group()
        self.stick = Mogistick(self)
        self.all_sprite.add(self.stick)
        self.mogichea.add(self.stick)
        self.mogi_num = 2
        self.mogi_kill = 0
        self.stop = True

    def run(self):
        self.opning()
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
        self.all_sprite.update()
        if len(self.mogi) < self.mogi_num:
            self.mogi_sprite = Mogi(self)
            self.all_sprite.add(self.mogi_sprite)
            self.mogi.add(self.mogi_sprite)
            self.mogi_kill += 1



    def draw(self):
        self.screen.fill(pygame.Color('White'))
        self.all_sprite.draw(self.screen)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def opning(self):
        self.draw_text('어느 날... 별 차이 없는 평범한 날.. 흘러나오는 뉴스..', 20, pygame.Color('Blue'), 150, 30)
        self.draw_text('"최근, 모기의 개체수가 급격하게 늘어났습니다."  "모기의 수가 거의 2배 가까이 늘었다고 콰이스트 연구진은 말했습니다."', 20, pygame.Color('Blue'), 340, 60)
        self.draw_text('', 20, pygame.Color('Blue'), 140, 30)
        pygame.display.flip()
        self.stop = True
        while self.stop:
            self.clock.tick(60)
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[pygame.K_SPACE]:
                self.stop = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = False
                    self.playing = False


game = Game()
game.run()
pygame.quit()