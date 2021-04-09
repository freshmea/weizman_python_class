import random
c = random.Random(100)

class Abc(object):
    def __init__(self):
        self.first = 'first string'
        pass
    def printx(self):
        print(self.first)
        pass

    pass
d = Abc()

# 타입의 데이터에 대한 정보입니다.
a = [40, int(40), '40', int('40'), 's', 39.99, True, [], {}, (), None, 0x10, object, c, d]

for i in a:
    print(f'변수는 {str(i)[:10]:10} 이고 변수의 타입은 {str(type(i)):20}이다.그리고 id 는 {str(id(i))[:10]:10} 이다.')



# print( a, b, c, d,  type(a), type(b), type(c), type(d))

a = float(123)
b = float(123.)
print(type(a), type(b))
print(a, b)
print(d.first)
d.printx()
d.first='second string'
print(d.first)
d.printx()

string='보물'
string2='황금'
print(f'변수에는 {string}과 {string2} 가 들어 있다.')

