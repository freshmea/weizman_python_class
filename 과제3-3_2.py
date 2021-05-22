# 5개의 인수(argument)를 받아서 숫자를 곱해서 출력하고 문자로 입력 받으면 에러를 출력하는 함수를 작성하세요.

def func1(a, b, c, d, e):
    if str(a).isdigit() and str(b).isdigit() and str(c).isdigit() and str(d).isdigit() and str(e).isdigit():
        print('???')
        return a * b * c * d * e
    return 'error'


print(func1(1, 2, 3, 4, 'a'))


# 5개의 인수중 2개는 키워드인수(keyword argument)로 받아서 5개를 곱해서 돌려주는 함수를 만드세요.

def func2(a, b, c, d=5, e=10):
    return a * b * c * d * e


print(func2(1, 2, 3))
print(func2(1, 2, 3, 4))
print(func2(1, 2, 3, e=4))


# 몬스터 클래스를 만들어서 공격을 당하면 몬스터의 피가 깍이는 코드를 만들어 보세요.

class Monster:
    def __init__(self, hp):
        self.hp = hp

    def attacked(self, attack):
        self.hp -= attack

    def state(self):
        if self.hp > 0:
            print(f'몬스터의 체력은{self.hp} 입니다.')
        else:
            print('몬스터가 죽었습니다.')


mon1 = Monster(100)

for i in range(10):
    mon1.state()
    mon1.attacked(15)
