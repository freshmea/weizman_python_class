def __init__(self, name, age):
    self._name = name
    self._age= age


class Descriptor:
    def __set_name__(self, owner, name):
        self._name = '_'+name

    def __get__(self, other, owner):
        return other.__dict__[self._name]

    def __set__(self, other, value):
        other.__dict__[self._name] = value

def decorator(cls):
    cls.__init__ = __init__
    return cls

@decorator
class Klass:
    name = Descriptor()
    age = Descriptor()

k=Klass()

print(k._name, k._age)
print(k.name, k.age)