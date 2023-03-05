"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker():

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

w1 = Position('Жаринов', 'Михаил', 'мастер', 1200, 300)
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


