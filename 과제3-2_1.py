# while 문 연습
count = 0
while count < 5:
    print(count)
    count = count + 1

# while else 문 연습
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# break 문 연습

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# continue 문 엽습

# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1

# 다음은 함수는 숫자를 입력 받아서 1부터 그 숫자까지 나누어지는 수들을 출력 합니다.

result = True
def primes1(number):
    prime=[]
    for i in range(2, number+1):
        result = True
        for j in range(2,i):
            if i%j == 0:
                result = False
        if result:
            prime.append(i)
    print(prime)
def primes2(number):
    a=[False, False]+[True]*(number-1)
    prime=[]
    for i in range(2, number+1):
        if a[i]:
            prime.append(i)
            for j in range(2*i, number+1, i):
                a[j]=False
    print(prime)


primes2(10000)
primes1(10000)