# import matplotlib.pyplot as plt
#
# months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# temp_f1=[15, 16, 18, 21, 24, 27, 28, 26, 23, 19, 16, 11]
# temp_ny=[2,2,4,11,16,22,25,26,24, 14, 12, 3]
#
# plt.plot(months, temp_f1, marker="o", color='red', linestyle=':', label='FL')
# plt.plot(months, temp_ny, marker='*', color='blue', linestyle=':', label='NY')
# plt.xlabel('Month')
# plt.ylabel('Celcius Temperature')
# plt.title('Monthly Temperature in temp_f1')
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