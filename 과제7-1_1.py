# # 파이게임 기본(클래스)

import pygame
import random
vec = pygame.math.Vector2

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60


class Ui(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.groups = self.game.ui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((SCREEN_X, SCREEN_Y))
        self.rect = self.image.get_rect()
        self.image.set_colorkey('Black')
        self.ui_health = self.game.snake.score

    def update(self):
        self.image.fill('Black')
        pygame.draw.rect(self.image, 'Gray', (10,10, SCREEN_X-20, SCREEN_Y-20), 10, 10)
        self.ui_health = self.game.snake.score
        pygame.draw.line(self.image, 'Red', (100, SCREEN_Y-100), (100+self.ui_health*3, SCREEN_Y-100), 15)
        self.draw_text(f'먹은 사과 수: {self.ui_health}', 30, pygame.Color('Red'), 100, SCREEN_Y -100)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_surface, text_rect)



class Apple(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('png/apple.svg')
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(random.randint(0,SCREEN_X), random.randint(0,SCREEN_Y))
        self.vel = vec(0,0)
        self.speed = 2

    def update(self):
        self.vel = (self.pos-self.game.snake.pos).normalize()*self.speed
        self.pos += self.vel
        self.rect.center = self.pos
        if self.collide():
            self.game.snake.score += 1
            self.kill()
            del self
            return
        if self.out():
            self.kill()
            del self
            return
    def collide(self):
        return pygame.sprite.spritecollide(self, self.game.snakes, False)

    def out(self):
        if (self.pos.x< 0 or self.pos.x>SCREEN_X):
            return True
        if (self.pos.y < 0 or self.pos.y > SCREEN_Y):
            return True
        return False


class Rotten(Apple):
    def __init__(self, root):
        Apple.__init__(self, root)
        self.image.fill('Black')

    def update(self):
        self.vel = (self.pos-self.game.snake.pos).normalize()*self.speed
        self.pos -= self.vel
        self.rect.center = self.pos
        if self.collide():
            self.game.snake.score -= 1
            self.kill()
            del self
            return



class Snake(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('png/snake-a.png')
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.snakes
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(SCREEN_X/2, SCREEN_Y/2)
        self.score = 0
        self.speed = 10

    def update(self):
        if self.game.pressed_key[pygame.K_UP]:
            self.pos.y += -self.speed
        if self.game.pressed_key[pygame.K_DOWN]:
            self.pos.y += self.speed
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x += -self.speed
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += self.speed
        self.rect.center = self.pos

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('스네이이크 게임')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprite = pygame.sprite.Group()
        self.snakes = pygame.sprite.Group()
        self.rottens = pygame.sprite.Group()
        self.snake = Snake(self)
        self.snakes.add(self.snake)
        self.all_sprite.add(self.snake)
        self.pressed_key = pygame.key.get_pressed()
        self.bg = pygame.image.load('png/BG/BG.png')
        self.bg = pygame.transform.scale(self.bg, (SCREEN_X, SCREEN_Y))
        self.ui = pygame.sprite.GroupSingle()
        self.ui.add(Ui(self))

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        # 종료 코드
        self.pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        if len(self.all_sprite)<20:
            self.all_sprite.add(Apple(self))
        if len(self.rottens)<3:
            self.rottens.add(Rotten(self))
        self.all_sprite.update()
        self.ui.update()
        self.rottens.update()

    def draw(self):
        self.screen.fill('white')
        self.screen.blit(self.bg, (0,0))
        self.all_sprite.draw(self.screen)
        self.rottens.draw(self.screen)
        self.ui.draw(self.screen)


game = Game()
game.run()
pygame.quit()
