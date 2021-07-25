# 날아다니는 새 에니메이션 추가 하기
# 자신의 게임 코드에 넣어서 추가해 보세요.
# 새 이미지는 png/bird (1).png, png/bird (2).png,png/bird (3).png, png/bird (4).png, png/bird (5).png,

# Bird 클래스 만들기(스프라이트 클래스 상속)
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.game = root
        self.groups = self.game.birds
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

# 게임 클래스에서 변경해야 될 것.

class Game:
    def __init__(self):
        self.birds = pygame.sprite.Group() # bird 클래스 만들기

    def load_data(self):
        # 새 이미지 불러오고 크기 조정하기
        self.birds_images = [pygame.image.load(f'png/bird ({x}).png').convert_alpha() for x in range(1, 6)]
        for image in self.birds_images:
            self.birds_images[self.birds_images.index(image)] = pygame.transform.scale(image, (100, 50))

    def update(self):
        # 새 클래스를 만들고 스프라이트에 넣기
        while len(self.birds.sprites()) < 10:
            self.birds.add(Bird(0, random.randint(1, 20) * SCREEN_Y / 20, self))
        # 모든 스프라이트 업데이트
        self.birds.update()

    def draw(self):
        # 모든 스프라이트 그리기
        self.birds.draw(self.screen)

