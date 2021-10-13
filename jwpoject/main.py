import pygame
import random
vec = pygame.math.Vector2

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 410 * 2  # 화면 높이
FPS = 60


def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont('malgungothic', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    surface.blit(text_surface, text_rect)

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
        pygame.draw.rect(self.image, 'Gray', (20,20, SCREEN_X-50, SCREEN_Y-50), 10, 10)
        self.ui_health = self.game.snake.score
        pygame.draw.line(self.image, 'blue', (100, SCREEN_Y-65),  (100+self.ui_health*3, SCREEN_Y-65), 15)
        draw_text(self.image, f'사과를 먹은수{self.ui_health}', 30, pygame.Color('blue'), 100, SCREEN_Y -65)
        draw_text(self.image, f'40/경과시간{int(pygame.time.get_ticks()/1000)}', 30, pygame.Color('blue'), 400, SCREEN_Y -65)



class Apple(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('apple.png').convert_alpha()
        self.image_d = pygame.image.load('apple2.png').convert_alpha()
        self.image_f = pygame.image.load('apple3.png').convert_alpha()
        self.image_dog = pygame.image.load('fffff.svg').convert_alpha()
        self.rect = self.image.get_rect()
        self.game = root
        self.groups= self.game.all_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(random.randint(0,SCREEN_X), random.randint(0, SCREEN_Y))
        self.speed = random.randint(3,10)
        self.dir =vec(1-random.random()*2, 1-random.random()*2)
        self.ifd = random.randint(0,12)
        self.lucky = random.randint(0,31)
        self.dog = random.randint(0,38)

    def update(self):
        if self.ifd == 0:
            self.image = self.image_d
        if self.lucky == 0:
            self.image = self.image_f
        if self.dog ==0:
            self.image = self.image_dog
        self.pos +=self.dir * self.speed
        self.rect.center = self.pos
        if self.collide():
            if self.ifd ==0:
                self.game.snake.score -= 5
            if self.lucky ==0:
                self.game.snake.score +=10
            if self.dog ==0:
                self.game.snake.score -=100
            self.game.snake.score += 1
            self.game.hit_sound.play()
            self.kill()
            del self
            return
        if self.pos.x< 0 or self.pos.x>SCREEN_X:
            self.kill()
            del self
            return
        if self.pos.y < 0 or self.pos.y > SCREEN_Y:
            self.kill()
            del self
            return

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
        self.speed = 9

    def update(self):
        self.image = self.images[self.index]
        if pygame.time.get_ticks()- self.time > 100:
            self.index += 1
            self.time = pygame.time.get_ticks()
        if self.index >= len(self.images):
            self.index = 0
        if self.game.pressed_key[pygame.K_UP]:
            self.pos.y += -self.speed
        if self.game.pressed_key[pygame.K_DOWN]:
            self.pos.y += self.speed
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x += -self.speed
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += self.speed
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
        self.bg = pygame.image.load('Light.svg')
        self.bg = pygame.transform.scale(self.bg, (SCREEN_X, SCREEN_Y))
        self.hit_sound = pygame.mixer.Sound('Collect.wav')
        pygame.mixer.music.load('Medieval2.mp3')
        self.acom = False
        self.sucimage = pygame.image.load('Dot-a.svg').convert_alpha()
        self.a = pygame.image.load('Dot-d.svg').convert_alpha()

    def run(self):
        pygame.mixer.music.play(-1)
        self.opening()
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
        self.ending()

    def opening(self):
        self.screen.fill('Black')
        draw_text(self.screen, f'snake and apple', 100, pygame.Color('Skyblue'), SCREEN_X / 2-300, SCREEN_Y / 2)
        draw_text(self.screen, f'시작할땐 스페이스,결과가 나오고 스페이스를 누르면 종료됩니다', 30, pygame.Color('Skyblue'), SCREEN_X / 2 - 300, SCREEN_Y / 2+200)
        draw_text(self.screen, f'snake는 방향키로 조작합니다.', 30, pygame.Color('Skyblue'), SCREEN_X / 2 - 300, SCREEN_Y / 2+300)
        pygame.display.update()
        stop = True
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[pygame.K_SPACE]:
                stop = False

    def ending(self):
        self.screen.fill('Black')
        if self.acom ==True:
            draw_text(self.screen, f'', 30, pygame.Color('Skyblue'),SCREEN_X /2, SCREEN_Y /2)
            self.screen.blit(self.sucimage ,(300,300))
        else:
            draw_text(self.screen, f'', 30, pygame.Color('Gray'), SCREEN_X / 2, SCREEN_Y / 2)
            self.screen.blit(self.a , (500, 500))
        pygame.display.update()
        stop = True
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[pygame.K_SPACE]:
                stop = False


    def event(self):
        # 종료 코드
        self.pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        if len(self.all_sprite) < 25:
            self.all_sprite.add(Apple(self))
        self.all_sprite.update()
        self.ui.update()
        if self.snake.score >= 100:
            self.playing = False
            self.acom = True
        if pygame.time.get_ticks()>40000 or self.snake.score < -10:
            self.playing = False
            self.acom = False

    def draw(self):
        self.screen.fill('white')
        self.screen.blit(self.bg, (0, 0))
        self.all_sprite.draw(self.screen)
        self.ui.draw(self.screen)



game = Game()
game.run()
pygame.quit()