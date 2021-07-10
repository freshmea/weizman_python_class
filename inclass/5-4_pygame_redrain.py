# 파이게임 비 내리는 코드(클래스)
import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 5
RAIN_NUMBER = 10
TITLE = '구름에서 비가 내리는 게임'
CHARACTER_SPEED = 5
# 컬러 예시 pygame.Color('name') colordict.py 에 컬러 이름 나열됨 name ='aliceblue', 'antiquewhite', 'antiquewhite1',
# 'antiquewhite2', 'antiquewhite3', 'antiquewhite4', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3',
# 'aquamarine4', 'azure', 'azure1', 'azure3', 'azure2', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3',
# 'bisque4', 'black', 'blanchedalmond', 'blue', 'blue1', 'blue2', 'blue3', 'blue4', 'blueviolet', 'brown', 'brown1',
# 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadetblue',
# 'cadetblue1', 'cadetblue2', 'cadetblue3', 'cadetblue4', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3',
# 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2',
# 'coral3', 'coral4', 'cornflowerblue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan',
# 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgoldenrod1', 'darkgoldenrod2',
# 'darkgoldenrod3', 'darkgoldenrod4', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta',
# 'darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3', 'darkolivegreen4', 'darkorange',
# 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4', 'darkorchid', 'darkorchid1', 'darkorchid2',
# 'darkorchid3', 'darkorchid4', 'darkred', 'darksalmon', 'darkseagreen', 'darkseagreen1', 'darkseagreen2',
# 'darkseagreen3', 'darkseagreen4', 'darkslateblue', 'darkslategray', 'darkslategray1', 'darkslategray2',
# 'darkslategray3', 'darkslategray4', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deeppink1',
# 'deeppink2', 'deeppink3', 'deeppink4', 'deepskyblue', 'deepskyblue1', 'deepskyblue2', 'deepskyblue3',
# 'deepskyblue4', 'dimgray', 'dimgrey', 'dodgerblue', 'dodgerblue1', 'dodgerblue2', 'dodgerblue3', 'dodgerblue4',
# 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floralwhite', 'forestgreen', 'gainsboro',
# 'ghostwhite', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3',
# 'goldenrod4', 'gray', 'gray0', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9',
# 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20',
# 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31',
# 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray41', 'gray42',
# 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53',
# 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64',
# 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75',
# 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86',
# 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray96', 'gray97',
# 'gray98', 'gray99', 'gray100', 'green', 'green1', 'green2', 'green3', 'green4', 'greenyellow', 'grey', 'grey0',
# 'grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8', 'grey9', 'grey10', 'grey11', 'grey12',
# 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19', 'grey20', 'grey21', 'grey22', 'grey23',
# 'grey24', 'grey25', 'grey26', 'grey27', 'grey28', 'grey29', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34',
# 'grey35', 'grey36', 'grey37', 'grey38', 'grey39', 'grey40', 'grey41', 'grey42', 'grey43', 'grey44', 'grey45',
# 'grey46', 'grey47', 'grey48', 'grey49', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56',
# 'grey57', 'grey58', 'grey59', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65', 'grey66', 'grey67',
# 'grey68', 'grey69', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74', 'grey75', 'grey76', 'grey77', 'grey78',
# 'grey79', 'grey80', 'grey81', 'grey82', 'grey83', 'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89',
# 'grey90', 'grey91', 'grey92', 'grey93', 'grey94', 'grey95', 'grey96', 'grey97', 'grey98', 'grey99', 'grey100',
# 'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hotpink', 'hotpink1', 'hotpink2', 'hotpink3',
# 'hotpink4', 'indianred', 'indianred1', 'indianred2', 'indianred3', 'indianred4', 'ivory', 'ivory1', 'ivory2',
# 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavenderblush', 'lavenderblush1',
# 'lavenderblush2', 'lavenderblush3', 'lavenderblush4', 'lawngreen', 'lemonchiffon', 'lemonchiffon1',
# 'lemonchiffon2', 'lemonchiffon3', 'lemonchiffon4', 'lightblue', 'lightblue1', 'lightblue2', 'lightblue3',
# 'lightblue4', 'lightcoral', 'lightcyan', 'lightcyan1', 'lightcyan2', 'lightcyan3', 'lightcyan4', 'lightgoldenrod',
# 'lightgoldenrod1', 'lightgoldenrod2', 'lightgoldenrod3', 'lightgoldenrod4', 'lightgoldenrodyellow', 'lightgray',
# 'lightgreen', 'lightgrey', 'lightpink', 'lightpink1', 'lightpink2', 'lightpink3', 'lightpink4', 'lightsalmon',
# 'lightsalmon1', 'lightsalmon2', 'lightsalmon3', 'lightsalmon4', 'lightseagreen', 'lightskyblue', 'lightskyblue1',
# 'lightskyblue2', 'lightskyblue3', 'lightskyblue4', 'lightslateblue', 'lightslategray', 'lightslategrey',
# 'lightsteelblue', 'lightsteelblue1', 'lightsteelblue2', 'lightsteelblue3', 'lightsteelblue4', 'lightyellow',
# 'lightyellow1', 'lightyellow2', 'lightyellow3', 'lightyellow4', 'linen', 'limegreen', 'magenta', 'magenta1',
# 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'mediumaquamarine',
# 'mediumblue', 'mediumorchid', 'mediumorchid1', 'mediumorchid2', 'mediumorchid3', 'mediumorchid4', 'mediumpurple',
# 'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4', 'mediumseagreen', 'mediumslateblue',
# 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'mistyrose1',
# 'mistyrose2', 'mistyrose3', 'mistyrose4', 'moccasin', 'navajowhite', 'navajowhite1', 'navajowhite2',
# 'navajowhite3', 'navajowhite4', 'navy', 'navyblue', 'oldlace', 'olivedrab', 'olivedrab1', 'olivedrab2',
# 'olivedrab3', 'olivedrab4', 'orange', 'orange1', 'orange2', 'orange3', 'orange4', 'orangered', 'orangered1',
# 'orangered2', 'orangered3', 'orangered4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'palegreen',
# 'palegreen1', 'palegreen2', 'palegreen3', 'palegreen4', 'palegoldenrod', 'paleturquoise', 'paleturquoise1',
# 'paleturquoise2', 'paleturquoise3', 'paleturquoise4', 'palevioletred', 'palevioletred1', 'palevioletred2',
# 'palevioletred3', 'palevioletred4', 'papayawhip', 'peachpuff', 'peachpuff1', 'peachpuff2', 'peachpuff3',
# 'peachpuff4', 'peru', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4',
# 'powderblue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red1', 'red2', 'red3', 'red4',
# 'rosybrown', 'rosybrown1', 'rosybrown2', 'rosybrown3', 'rosybrown4', 'royalblue', 'royalblue1', 'royalblue2',
# 'royalblue3', 'royalblue4', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'saddlebrown', 'sandybrown',
# 'seagreen', 'seagreen1', 'seagreen2', 'seagreen3', 'seagreen4', 'seashell', 'seashell1', 'seashell2', 'seashell3',
# 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'skyblue', 'skyblue1', 'skyblue2', 'skyblue3',
# 'skyblue4', 'slateblue', 'slateblue1', 'slateblue2', 'slateblue3', 'slateblue4', 'slategray', 'slategray1',
# 'slategray2', 'slategray3', 'slategray4', 'slategrey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'springgreen',
# 'springgreen1', 'springgreen2', 'springgreen3', 'springgreen4', 'steelblue', 'steelblue1', 'steelblue2',
# 'steelblue3', 'steelblue4', 'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3',
# 'thistle4', 'tomato', 'tomato1', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2',
# 'turquoise3', 'turquoise4', 'violet', 'violetred', 'violetred1', 'violetred2', 'violetred3', 'violetred4', 'wheat',
# 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'whitesmoke', 'yellow', 'yellow1', 'yellow2', 'yellow3',
# 'yellow4', 'yellowgreen'


class Player:
    def __init__(self, root):
        self.x = 100
        self.y = SCREEN_Y-300
        self.dx = 0
        self.dy = 0
        self.root = root
        self.image = root.player_image
        self.hit = 0
        self.redhit = 0

    def move(self, key):
        if key == pygame.K_UP:
            self.dy = -CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_DOWN:
            self.dy = CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_LEFT:
            self.dx = -CHARACTER_SPEED
            self.dy = 0
        if key == pygame.K_RIGHT:
            self.dx = CHARACTER_SPEED
            self.dy = 0

        if 0 < self.x < SCREEN_X:
            self.x += self.dx
        else:
            self.dx *= -1
            self.x += self.dx

        if 0 < self.y < SCREEN_Y:
            self.y += self.dy
        else:
            self.dy *= -1
            self.y += self.dy

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, rain):
        return pygame.Rect(self.x+50, self.y+20, 120, 200).collidepoint((rain.x, rain.y))


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('skyblue')
        self.red = random.randint(0, 100)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > SCREEN_Y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)
        if self.red == 0:
            pygame.draw.line(self.game.screen, pygame.Color('red'), (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = 50
        self.game = root
        self.image = root.cloud_image
        self.speed = random.randint(2, 10)

    def move(self):
        if self.x >= SCREEN_X:
            self.x = 1
        self.x += self.speed

    def rain(self):
        for _ in range(RAIN_NUMBER):
            self.game.rains.append(Rain(random.randint(self.x, self.x + 130), self.y + 70, self.game))

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.rains = []
        self.clouds = []
        self.player = Player(self)

    def load_data(self):
        # 배경그림 불러오기
        self.image_background = pygame.image.load('../images/back.png').convert_alpha()
        self.image_background = pygame.transform.scale(self.image_background, (SCREEN_X, SCREEN_Y))
        # 구름그림 불러오기
        self.cloud_image = pygame.image.load('../images/cloud.svg').convert_alpha()
        self.player_image = pygame.image.load('../images/cloud.svg').convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (200, 300))

    def run(self):
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
                if event.key == pygame.K_q:
                    self.playing = False
                self.player.move(event.key)

    def update(self):
        # 구름 생성
        while len(self.clouds) < CLOUD_NUMBER:
            self.clouds.append(Cloud(random.randint(1, 20) * SCREEN_X / 20, self))
        # 구름에서 비 생성하고 구름 움직이기
        for cloud in self.clouds:
            cloud.rain()
            cloud.move()
        # 비를 움직이게 하고 화면 밖으로 가면 제거 하기
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 플레이어 움직임
        self.player.move(None)
        # 플레이어가 비 맞음 체크
        for rain in self.rains:
            if self.player.hit_by(rain):
                self.player.hit += 1
                if rain.red == 0:
                    self.player.redhit += 1
                self.rains.remove(rain)
                del rain

    def draw(self):
        # self.screen.fill((255, 255, 255))
        # 배경화면 그리기
        self.screen.blit(self.image_background, (0, 0))
        # 구름 그리기
        for cloud in self.clouds:
            cloud.draw()
        # 비 그리기
        for rain in self.rains:
            rain.draw()
        # 플레이어 그리기
        self.player.draw()
        # 글자 출력
        self.draw_text(f'빨간비에 맞은 수: {self.player.redhit}   비에 맞은 수{self.player.hit}', 30, pygame.Color('hotpink'), SCREEN_X / 4, SCREEN_Y * 1 / 400)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


game = Game()
game.run()
pygame.quit()
