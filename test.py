


class Rgb:
    def __init__(self, r, g, b):
        self.r =r
        self.g =g
        self.b =b

    def __add__(self, other):
        self.r += other.r
        self.g += other.g
        self.b += other.b


    def pr(self):
        print(self.r, self.g, self.b)

a=Rgb(1,2,3)
b=Rgb(23,13,13)

c=a+b
a.pr()
b.pr()
print(type(c))
