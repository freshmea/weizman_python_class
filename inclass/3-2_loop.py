# 구구단을 출력하자.

print('구구단입니다.')

for i in range(9):
    print(f'{i+1} 단 의 구구단 입니다.')
    for j in range(9):
        print(f'{i+1} X {j+1} = {(i+1)*(j+1)} 입니다.')
#
# 5354
# --->
# ♥♥♥♥♥
# ♥♥♥
# ♥♥♥♥♥
# ♥♥♥♥
# 432
# ---->
# ♥♥♥♥
# ♥♥♥
# ♥♥
#
# 123
# ----->
# ♥
# ♥♥
# ♥♥♥
#


#하트를 출력하자.
#이중 for 문을 이용하세요.

a= input('숫자를 입력하라')

for i in a:
    for j in range(int(i)):
        print('♥', end='')
    print()