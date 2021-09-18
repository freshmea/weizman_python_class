import pygame
import random
vec = pygame.math.Vector2

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 410 * 2  # 화면 높이
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
        pygame.draw.rect(self.image, 'Gray', (25,30, SCREEN_X-50, SCREEN_Y-50), 10, 10)
        self.ui_health = self.game.snake.score
        pygame.draw.line(self.image, 'blue', (100, SCREEN_Y-65),  (100+self.ui_health*3, SCREEN_Y-65), 15)
        self.draw_text(f'사과를 먹은수{self.ui_health}', 30, pygame.Color('blue'), 100, SCREEN_Y -65)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_surface, text_rect)


class Apple(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('apple.png').convert_alpha()
        self.image_d = pygame.image.load('apple2.png').convert_alpha()
        self.image_f = pygame.image.load('apple3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.game = root
        self.groups= self.game.all_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(random.randint(0,SCREEN_X), random.randint(0, SCREEN_Y))
        self.speed = random.randint(1,5)
        self.dir =vec(1-random.random()*2, 1-random.random()*2)
        self.ifd = random.randint(0,2)
        self.lucky = random.randint(0,20)
    def update(self):
        if self.ifd == 0:
            self.image = self.image_d
        if self.lucky == 0:
            self.image = self.image_f
        self.pos +=self.dir * self.speed
        self.rect.center = self.pos
        if self.collide():
            if self.ifd ==0:
                self.game.snake.score -= 5
            if self.lucky ==0:
                self.game.snake.score +=10
            self.game.snake.score += 1
            self.game.hit_sound.play()
            self.kill()
            del self

    def collide(self):
        return pygame.sprite.spritecollide(self, self.game.snakes, False)

class Snake(pygame.sprite.Sprite):
    def __init__(self, root):
        self.images = []
        self.images.append(pygame.image.load('Snake-a7.png').convert_alpha())
        self.images.append(pygame.image.load('Snake-a6.png').convert_alpha())
        self.images.append(pygame.image.load('Snake-a5.png').convert_alpha())
        self.images.append(pygame.image.load('Snake-a4.png').convert_alpha())
        self.images.append(pygame.image.load('Snake-a2.png').convert_alpha())
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.game = root
        self.groups= self.game.all_sprite, self.game.snakes
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(SCREEN_X/2, SCREEN_Y/2)
        self.score = 0
        self.index = 0
        self.time = 0

    def update(self):
        self.image = self.images[self.index]
        if pygame.time.get_ticks()- self.time > 1000:
            self.index += 1
            self.time = pygame.time.get_ticks()
        if self.index >= len(self.images):
            self.index = 0
        if self.game.pressed_key[pygame.K_UP]:
            self.pos.y += -9
        if self.game.pressed_key[pygame.K_DOWN]:
            self.pos.y += 9
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x += -9
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += 9
        self.rect.center =self.pos




class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('스네이크 게임')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprite = pygame.sprite.Group()
        self.snakes = pygame.sprite.Group()
        self.snake = Snake(self)
        self.all_sprite.add(self.snake)
        self.snakes.add(self.snake)
        self.ui = pygame.sprite.GroupSingle()
        self.ui.add(Ui(self))
        self.pressed_key = pygame.key.get_pressed()
        self.bg = pygame.image.load('Stripes.png')
        self.bg = pygame.transform.scale(self.bg, (SCREEN_X, SCREEN_Y))
        self.hit_sound = pygame.mixer.Sound('Collect.wav')
        pygame.mixer.music.load('Medieval2.mp3')

    def run(self):
        pygame.mixer.music.play(-1)
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
        if len(self.all_sprite) < 1000:
            self.all_sprite.add(Apple(self))
        self.all_sprite.update()
        self.ui.update()

    def draw(self):

        self.screen.fill('white')
        self.screen.blit(self.bg, (0, 0))
        self.all_sprite.draw(self.screen)
        self.ui.draw(self.screen)



game = Game()
game.run()
pygame.quit()