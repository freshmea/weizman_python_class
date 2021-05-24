# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# import numpy as np
# import pygame
#
# # path= '../fonts/malgun.ttf'
# # font_name = fm.FontProperties(fname=path, size=18).get_name()
# # plt.rc('font', family=font_name)
#
# x = np.linspace(0, 4 * np.pi, 2000)
# y = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)
#
# plt.plot(x, y, color='red', label='sine')
# plt.plot(x, y2, color='blue', label='cosine')
# plt.plot(x, y3, label='tangent')
# plt.ylim(-2, 2)
# plt.xlabel('x')
# plt.ylabel('y')
# # plt.title('삼각함수')
#
# plt.legend(loc='upper left')
# plt.grid(True)
# plt.draw()

# fig = plt.gcf()
# fig.savefig('11.png', dpi=fig.dpi)
#
# pygame.init()
# win = pygame.display.set_mode((600, 600))
# pygame.display.set_caption("image test")
# clock = pygame.time.Clock()
#
# img = pygame.image.load('11.png')
# while True:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     win.fill((255,255,255))
#     win.blit(img, (0, 0))
#     pygame.display.update()
#
