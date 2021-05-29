# #삼각 함수 그리기
# import matplotlib.pyplot as plt
# import numpy as np
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
#
# plt.legend(loc='upper left')
# plt.grid(True)
# plt.show()

# # 포물선 그리기
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-4, 4 , 2000)
# y = x*x
#
# print(x, y)
# plt.plot(x,y)
# plt.show()

# # 직선 그리기
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-4, 4 , 2000)
# #기울기
# a=1.5
# #y절편
# b=1
#
# y = a*x+b
#
# print(x, y)
# plt.plot(x,y)
# plt.grid(True)
# plt.ylim(-2, 2)
# plt.xlim(-2, 2)
# plt.show()

# 원 그리기
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 2000)

# 반지름
r = 3
y = (r * r - x * x) ** (1 / 2)
y2 = -(r * r - x * x) ** (1 / 2)
plt.plot(x, y, color='black')
plt.plot(x, y2, color='black')
plt.grid(True)
plt.ylim(-4, 4)
plt.xlim(-5, 5)
plt.show()
