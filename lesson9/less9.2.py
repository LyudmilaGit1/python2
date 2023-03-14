"""Создать метакласс для паттерна Синглтон (см. конец вебинара)"""

class Singleton(type):

    _a = None
    def __call__(cls, *args, **kwargs):
        if cls == None:
            cls._a = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._a

class Oneclass(metaclass=Singleton):
    pass

b = Oneclass()
c = Oneclass()

print(b is c)
print(id(b), id(c))





