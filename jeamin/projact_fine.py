import sys
import pygame
import random

## pygame initionalize
pygame.init()
pygame.font.init()

## GLOBAL VARIABLES
# Version
VERSION = '0.3'
# Resolution
WIDTH = 980
HEIGHT = 640
# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 12)
DARK_ORANGE = (196, 121, 67)
# SCENE
STARTSCREEN = 'start_screen'
PLAYGAME = 'play_game'
GAMEOVER = 'game_over'
QUIT = 'quit'
# OPTIONS
FPS = 60
# PyGame
screen = None
font_title = pygame.font.SysFont('malgungothic', 65)
font_big = pygame.font.SysFont('malgungothic', 36)
font_default = pygame.font.SysFont('malgungothic', 28)
SPEED = 1  # must int
KEYINTERVAL = 5
cscore = 0
START_TIME = 0

# sound
soundkid = pygame.mixer.music.load('img/bgmusic.wav')
soundkid1 = pygame.mixer.Sound("img/explosion.wav")
soundkid1.set_volume(0.25)
vec = pygame.Vector2


## MAIN
def main(argv):
    # pygame init
    pygame.init()
    # display
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # window titlebar
    pygame.display.set_caption('Dodge ' + VERSION)
    # start_game
    main_loop()


## MAIN_LOOP: MAIN_SCREEN
def main_loop():
    user_action = STARTSCREEN
    while user_action != QUIT:
        if user_action == STARTSCREEN:
            user_action = start_screen()
        elif user_action == PLAYGAME:
            user_action = play_game()
        elif user_action == GAMEOVER:
            soundkid1.play()
            user_action = game_over()
    pygame.quit()
    sys.exit(0)


## START_SCREEN
def start_screen():
    """
    https://www.pygame.org/docs/ref/key.html
    """
    global font_title
    global font_big
    global font_default
    global screen
    global cscore
    image_bg = pygame.image.load("img/spacebackground1.png")
    image_bg = pygame.transform.scale(image_bg, (WIDTH, HEIGHT))
    screen.blit(image_bg, (0, 0))
    draw_text('총알 피하기', font_title, screen,
              WIDTH / 2, HEIGHT / 3, RED, YELLOW)
    draw_text('준비가 되면 스페이스를 누르세요.', font_big, screen,
              WIDTH / 2, HEIGHT / 2, GREEN, BLACK)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return PLAYGAME
            elif event.key == pygame.K_ESCAPE:
                return QUIT
        elif event.type == pygame.QUIT:
            return QUIT
        cscore = 0
    return STARTSCREEN


## PLAYGAME
def play_game():
    global font_default
    global screen
    global cscore

    pygame.key.set_repeat(KEYINTERVAL)

    airplane = AirPlane()
    airplane.set_position((WIDTH / 2, HEIGHT / 2))
    bullets = pygame.sprite.Group()

    pygame.mixer.music.play(-1)
    while True:
        # fps
        fps_clock = pygame.time.Clock()
        fps_clock.tick(FPS)
        max_bullet = (pygame.time.get_ticks()-START_TIME)/1000
        screen.fill(BLACK)
        draw_text('{0} points'.format(cscore), font_default, screen,
                  WIDTH / 1.1, 20, DARK_ORANGE, None)
        draw_text('{0} bullets'.format(len(bullets)), font_default, screen,
                  WIDTH / 10, 20, DARK_ORANGE, None)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    return GAMEOVER
            elif event.type == pygame.QUIT:
                return QUIT
        airplane.set_position(pygame.mouse.get_pos())
        if airplane.collide(bullets):
            return GAMEOVER

        if len(bullets) < max_bullet:
            bullets.add(random_bullet())
        bullets.update()
        bullets.draw(screen)
        screen.blit(airplane.image, airplane.rect)
        pygame.display.update()


## GAMEOVER
def game_over():
    global font_big
    global font_default
    global screen
    global cscore
    pygame.mixer.music.stop()
    screen.fill(BLACK)
    image_bg = pygame.image.load("img/gkgkgkgkgkgkgkgkgkkgkgkgkgkg.png")
    image_bg = pygame.transform.scale(image_bg, (WIDTH, HEIGHT))
    screen.blit(image_bg, (0, 0))
    draw_text('GAME OVER', font_big, screen,
              WIDTH / 2, HEIGHT / 4, RED, WHITE)
    draw_text('Score: {0}'.format(cscore), font_default, screen,
              WIDTH / 2, HEIGHT / 3, GREEN, WHITE)
    draw_text('Press Enter for back to main menu', font_default, screen,
              WIDTH / 2, HEIGHT / 2, WHITE, None)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(BLACK)
                return STARTSCREEN
        elif event.type == pygame.QUIT:
            return QUIT
    return GAMEOVER


### DRAW_TEXT
def draw_text(text, font, surface, x, y, main_color, back_color):
    """
    https://www.pygame.org/docs/ref/font.html
    https://www.pygame.org/docs/ref/surface.html
    """
    textobject = font.render(text, True, main_color, back_color)
    textrect = textobject.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobject, textrect)


## AIRPLANE
class AirPlane(pygame.sprite.Sprite):
    def __init__(self):
        super(AirPlane).__init__()
        self.image = pygame.image.load("img/spaceship.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def set_position(self, pos):
        self.rect.topleft = pos

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
        return None


## BULLET
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.speed = random.randint(2,7)
        self.color = 'green'
        if self.speed == 6:
            self.color = 'red'
        if self.speed == 7:
            self.color = 'blue'
        pygame.draw.circle(self.image, self.color, self.rect.center, 5, 0)
        self.rect.topleft = pos
        self.dir = dir


    def update(self):
        self.rect.topleft += self.dir * self.speed
        if self.is_edge():
            global cscore
            cscore = cscore + 1
            self.kill()
            del self

    def is_edge(self):
        if self.rect.x > WIDTH:
            return True
        elif self.rect.x < 1:
            return True
        if self.rect.y > HEIGHT:
            return True
        elif self.rect.y < 1:
            return True
        return False


### RANDOMBULLET
def random_bullet():
    side = random.randint(1, 4)
    if side == 1:  # TOP
        xpos = random.randint(0, WIDTH)
        ypos = 1
        xspeed = random.uniform(-1, 1)
        yspeed = random.uniform(0, 1)
    elif side == 2:  # BOTTOM
        xpos = random.randint(0, WIDTH)
        ypos = HEIGHT
        xspeed = random.uniform(-1, 1)
        yspeed = random.uniform(-1, 0)
    elif side == 3:  # RIGHT
        xpos = WIDTH
        ypos = random.randint(0, HEIGHT)
        xspeed = random.uniform(-1, 0)
        yspeed = random.uniform(-1, 1)
    elif side == 4:  # LEFT
        xpos = 1
        ypos = random.randint(0, HEIGHT)
        xspeed = random.uniform(0, 1)
        yspeed = random.uniform(-1, 1)
    return Bullet(vec(xpos, ypos), vec(xspeed, yspeed).normalize())


if __name__ == '__main__':
    sys.exit(main(sys.argv))
