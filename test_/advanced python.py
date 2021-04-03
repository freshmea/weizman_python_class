from dataclasses import dataclass

class Klass(object):
    """연습용 클래스이다."""
    name='클래스 속성이다.'
    def __init__(self, name):
        self.name= name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name

class a(Klass):
    pass
print(globals())
p=Klass('choi su gil')
print(p.getName())
p.setName('객체속성이다.')
print(p.getName())

print(Klass.__dict__)
print(p.name)
print(Klass.name)

@dataclass
class person:
    name: str
    age: int

a=person('choi', 23)

print(a.__dict__)