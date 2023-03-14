"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time

class TrafficLight():

    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5


    red_color = 'красный'
    yellow_color = 'желтый'
    green_color = 'зеленый'

    def __init__(self, color):
        self.__color = color


    def switch_light(self, color, wait):
        self.wait = wait
        print(f'Включен {color} свет, время ожидания {self.wait} сек')
        time.sleep(self.wait)

    def running(self, color=''):

        while (input("Включить светофор?")) == "да":
            if not color:
                loc_color = self.__color
            else:
                loc_color = color

            if loc_color == self.red_color:
                self.switch_light('красный', self.red_color_wait)
                self.switch_light('желтый', self.yellow_color_wait)
                self.switch_light('зеленый', self.green_color_wait)


tl1 = TrafficLight('красный')
tl1.running()


