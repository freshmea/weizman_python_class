import pygame

# 스크린 전체 크기 지정

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame sount test")

# FPS를 위한 Clock 생성

clock = pygame.time.Clock()

# wav, mp3, ogg 가능
pygame.mixer.music.load('out.wav')

# wav, ogg 가능
sound_thunder = pygame.mixer.Sound('out.wav')

# Music stream 무한 반복
pygame.mixer.music.play(-1)

playing = True
while playing:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v + 0.1)
                print("volume up")

            if event.key == pygame.K_DOWN:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v - 0.1)
                print("volume down")

            if event.key == pygame.K_LEFT:
                pygame.mixer.music.pause()
                print("일시 멈춤")

            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.unpause()
                print("다시 재생")

            if event.key == pygame.K_a:
                sound_thunder.play()
                print("천둥소리")
            if event.key == pygame.K_b:
                sound_thunder.stop()
                print("천둥소리")

    # 1초에 60번의 빈도로 순환하기
    clock.tick(60)