import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
a_image = pygame.image.load('images/ben-a.svg')
font = pygame.font.SysFont('malgungothic', 36)
sound = pygame.mixer.Sound('wave/attention.wav')
sound.play()
y = 0
x = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        y -= 1
    if pressed_keys[pygame.K_s]:
        y += 1
    if pressed_keys[pygame.K_a]:
        x -= 1
    if pressed_keys[pygame.K_d]:
        x += 1

    screen.fill((255,255,255))
    screen.blit(a_image, (x ,y))
    a=font.render('안녕하세요!!!!', True, (255, 0, 0))
    screen.blit(a, (0,0))

    pygame.display.update()
