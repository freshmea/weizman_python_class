#시스템 폰트 찾는 방법
# for font in font_list:
#     fp=fm.FontProperties(fname=font)
#     fn=fp.get_name()
#     print("%s >> %s" %(fp,fn))



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
# plt.bar(pets, students, color=colors)
#
# plt.xlabel('Pets')
# plt.ylabel('Students')
# plt.title('Pets survey in class')
# plt.grid(axis='y')
#
# plt.show()

#plt.savefig('aaa.png')
import matplotlib.colors
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_list=fm.findSystemFonts()
path=font_list[font_list.index('C:\Windows\Fonts\malgun.ttf')]
font_name = fm.FontProperties(fname=path, size=18).get_name()
plt.rc('font', family=font_name)

countries = ['미국', '우크라이나', "중극", '러시아', '독일']
gold = [34, 53, 24, 54, 24]
silver = [23, 41, 32, 14, 34]
bronze = [23, 52, 34, 95, 13]
print(map(gold, silver))
bottom_silver = [a + 3 for a in gold]
bottom_bronze = [a + b + 6 for a, b in zip(gold, silver)]

fig, ax = plt.subplots()
p1 = ax.bar(countries, gold, color='gold', label='Gold')
p2 = ax.bar(countries, silver, bottom=bottom_silver, label='Silver')
p3 = ax.bar(countries, bronze, bottom=bottom_bronze, label='Bronze')

plt.xlabel('나라')
plt.ylabel('메달수')
plt.title('2015년 리오 올림픽')
plt.legend()

ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')
plt.show()

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
# countries = ['USA', 'GBR', "China", 'Russia', 'Germany']
# gold = [34, 53, 24, 54, 24]
# plt.pie(gold, labels=countries, autopct="%.1f%%")
# plt.title('medal')
# plt.show()

#
# import matplotlib.pyplot as plt
#
#
# countries = ['USA', 'GBR', "China", 'Russia', 'Germany']
# gold = [34, 53, 24, 54, 24]
# colors= ['red', 'green', 'blue', 'yellow', 'cyan']
# explode=[0, 0.1, 0, 0, 0]
#
# plt.pie(gold, explode=explode, labels=countries, colors=colors, autopct="%.1f%%")
# plt.title('medal')
# plt.show()