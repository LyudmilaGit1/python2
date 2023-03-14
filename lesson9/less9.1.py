"""Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
Создать метакласс для паттерна Синглтон (см. конец вебинара)"""
class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")

        instance.__dict__[self.attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.attr]

    def __set_name__(self, owner, attr):
        self.attr = attr

class Worker():
    wage = NonNegative()
    bonus = NonNegative()
    def __init__(self, name, surname, position, wage, bonus):

        self.name = name
        self.surname = surname
        self.position = position

        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus':  self.bonus}

class Position(Worker):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

w1 = Position('Жаринов', 'Михаил', 'мастер', 1200, -300)
w2 = Position('Кузнецов', 'Сергей', 'сварщик', 1000, 250)
def printing(arg):
    print('Фамилия', arg.surname)
    print('Имя', arg.name)
    print('Должность', arg.position)
    print('Полное имя', arg.get_full_name())
    print('Оклад, руб.', arg.wage)
    print('Размер премии', arg.bonus)
    print('Размер дохода, руб.', arg.get_total_income())


printing(w1)
print()
printing(w2)
