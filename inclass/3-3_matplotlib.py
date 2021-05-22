# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# path= '../fonts/malgun.ttf'
# font_name = fm.FontProperties(fname=path, size=18).get_name()
# plt.rc('font', family=font_name)
#
# months = [str(x+1)+'월' for x in range(12)]
# temp_f1 = [15, 16, 18, 21, 24, 27, 28, 26, 23, 19, 16, 11]
# temp_ny = [2, 2, 4, 11, 16, 22, 25, 26, 24, 14, 12, 3]
#
#
# plt.plot(months, temp_f1, marker="o", color='red', linestyle=':', label='FL')
# plt.plot(months, temp_ny, marker='*', color='blue', linestyle=':', label='NY')
# plt.xlabel('월')
# plt.ylabel('섭씨 온도')
# plt.title('서울의 월별 날씨')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
#
# pets=['Dog', 'Cat', 'Fish', 'Hamster', 'Rabbit']
# students=[11, 8, 5, 4, 2]
# colors=['red', 'green', 'blue', 'yellow', 'cyan']
#
# fig, ax = plt.subplots()
# container = ax.bar(pets, students, color=colors)
#
# plt.bar_label(container)
# plt.xlabel('Pets')
# plt.ylabel('Students')
# plt.title('Pets survey in class')
# plt.grid(axis='y')
#
# plt.show()
# #plt.savefig('aaa.png')

# import matplotlib.pyplot as plt
#
# countries = ['USA', 'GBR', "China", 'Russia', 'Germany']
# gold = [34, 53, 24, 54, 24]
# silver = [23, 41, 32, 14, 34]
# bronze = [23, 52, 34, 95, 13]
#
# bottom_silver = gold
# bottom_bronze = [a + b for a, b in zip(gold, silver)]
#
# fig, ax = plt.subplots()
# p1 = ax.bar(countries, gold, color='gold', label='Gold')
# p2 = ax.bar(countries, silver, bottom=bottom_silver, label='Silver')
# p3 = ax.bar(countries, bronze, bottom=bottom_bronze, label='Bronze')
#
# plt.xlabel('Countries')
# plt.ylabel('Medals')
# plt.title('Rio 2-15 Olympic')
#
# ax.bar_label(p1, label_type='center')
# ax.bar_label(p2, label_type='center')
# ax.bar_label(p3, label_type='center')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# countries = ['USA', 'GBR', "China", 'Russia', 'Germany']
# gold = [34, 53, 24, 54, 24]
# silver = [23, 41, 32, 14, 34]
# bronze = [23, 52, 34, 95, 13]
#
# x= np.arange(len(countries))
# width=.2
#
# fig, ax=plt.subplots()
# p1=ax.bar(x-width, gold, width)
# p2 =ax.bar(x, silver, width)
# p3= ax.bar(x+width, bronze, width)
# plt.show()

# import matplotlib.pyplot as plt
#
# countries = ['USA', 'GBR', "China", 'Russia', 'Germany']
# gold = [34, 53, 24, 54, 24]
#
# plt.pie(gold, labels=countries, autopct="%.1f%%")
# plt.title('Stock Sectores')
# plt.show()


import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pygame

# path= '../fonts/malgun.ttf'
# font_name = fm.FontProperties(fname=path, size=18).get_name()
# plt.rc('font', family=font_name)

x = np.linspace(0, 4 * np.pi, 2000)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.plot(x, y, color='red', label='sine')
plt.plot(x, y2, color='blue', label='cosine')
plt.plot(x, y3, label='tangent')
plt.ylim(-2, 2)
plt.xlabel('x')
plt.ylabel('y')
# plt.title('삼각함수')

plt.legend(loc='upper left')
plt.grid(True)
plt.draw()

fig = plt.gcf()
fig.savefig('11.png', dpi=fig.dpi)

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("image test")
clock = pygame.time.Clock()

img = pygame.image.load('11.png')
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    win.fill((255,255,255))
    win.blit(img, (0, 0))
    pygame.display.update()

