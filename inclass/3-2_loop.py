# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)
#
#
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break
#
# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1


# # 리스트
# for i in [1, 2, 3]:
#     print(i)
#
# # 튜플
# for i in (4, 5, 6):
#     print(i)
#
# # 집합
# for i in {1, 2, 3}:
#     print(i)
#
# # 튜플
# for i in 4, 5, 6:
#     print(i)
#
# # 딕션너리
# # for i in {1:2, 3:4, 5:6}
# #     print(i)
#
# a = 1
# for i in range(1000):
#     if a % 3 == 0 or a % 5 == 0:
#         print(a, end=' ')
#     a += 1
# print()
#
# a = range(5)
# for i in a:
#     print(i)
#
# a = range(1, 5)
# for i in a:
#     print(i)
#
# a = range(1, 15, 3)
# for i in a:
#     print(i)

# a = 0
# for i in range(15):
#     a += 1
#     if a == 10:
#         break
#     print(a, '번째 코드 실행')
# print('종료')
#
# a = 0
# for i in range(15):
#     a += 1
#     if a == 10:
#         continue
#     print(a, '번째 코드 실행')
# print('종료')

import time

playing = True
while playing:
    print('프로그램이 실행중이다.')
    time.sleep(1)
    a = input('프로그램을 종료할까요?[y/n]')
    if a == 'y':
        playing = False
    else:
        playging = True
print('프로그램을 종료합니다.')
