# # a=0
# # for i in range(1000):
# #     a +=1
# #     if a%3 == 0 or a%5 == 0:
# #         print(a, end='  ')
# #         if a%30 == 0:
# #             print()
# #
# #
# # #a=input('숫자를 입력하시오: ')
# #
# # # 산술 연산
# # a = 10
# # b = 3
# # print('a + b = ', a + b)
# # print('a - b = ', a - b)
# # print('a * b = ', a * b)
# # print('a / b = ', a / b)
# # print('a % b = ', a % b)
# # print('a // b = ', a // b)
# # print('a ** b = ', a ** b)
# #
# # # 관계 연산자
# # a = 10
# # b = 3
# # print(a > b)
# # print(a >= b)
# # print(a < b)
# # print(a > b)
# # print(a >= b)
# # print(a == b)
# # print(a != b)
# #


a= input('수를 입력하세요.')
a= int(a)

if 100<a<1000:
    print('작은수')
if 1000<a<10000:
    print('큰수')
if 10000<a:
    print('매우 큰수')
