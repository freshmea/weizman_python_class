# for i in range(0, 100):
#     print("아 ", '아', end='')
#     print('다시 파이썬을 공부해야 하다니... ㄷㄷ', end='', flush=True)

a=0
a=input('숫자를 넣어러:\n')
a=int(a)
print('1부터 숫자까지 모두 더해서 알려주마')
k=0
for i in range(1,a+1):
    print(i, a)
    k+= i
print(k)

#이것은 학원 컴퓨터에서 작업한 내용이다. 