a=0
for i in range(1000):
    a +=1
    if a%3 == 0 or a%5 == 0:
        print(a, end='  ')
        if a%30 == 0:
            print()


#a=input('숫자를 입력하시오: ')

# 산술 연산
a = 10
b = 3
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)
print('a % b = ', a % b)
print('a // b = ', a // b)
print('a ** b = ', a ** b)

# 관계 연산자
a = 10
b = 3
print(a > b)
print(a >= b)
print(a < b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

