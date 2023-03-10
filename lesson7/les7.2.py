"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
class Road():

    __weight = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width


    def all_weight(self, thickness):
        res = self.__length * self.__width * thickness * self.__weight
        return res


r2 = Road(5000, 20)
w2 = r2.all_weight(0.05)

print(f'20м*5000м*25кг*0.05м = {w2} кг =  {w2 / 1000} т')
