#변수지정
BLACK= (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)




def myfuc(a, b, type='+', repeat=1):
    result=0
    for i in range(repeat):
        if type =='+':
            result += a + b
        if type =='-':
            result += a - b
        if type =='*':
            result += a * b
        if type == '/':
            result += a / b
    return result


# number = myfuc(5, 1, type='/', repeat=2)
#
# print(number)


class Clac:
    def __init__(self, a, b):
        self.a= a
        self.b= b

    def plus(self):
        return self.a+self.b

    def minus(self):
        return self.a-self.b

    def multiple(self):
        return self.a*self.b

    def divide(self):
        return self.a/self.b

a= Clac(3,5)

# print(a.a, a.b, a.multiple(), a.plus(), a.minus(), a.divide())