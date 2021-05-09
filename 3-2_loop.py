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


#리스트
for i in [1, 2, 3]:
    print(i)

#튜플
for i in (4, 5, 6):
    print(i)

#집합
for i in {1,2,3}:
    print(i)

#튜플
for i in 4, 5, 6:
    print(i)

#딕션너리
# for i in {1:2, 3:4, 5:6}
#     print(i)

a=1
for i in range(1000):
    if a % 3 == 0 or a % 5 == 0:
        print(a, end = ' ')
    a += 1