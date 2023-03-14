"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции"""



def prints(lst):
    for i in lst:
        print(f"{type(i)},{i}")


words = ['разработка', 'сокет', 'декоратор']
point_u = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                '\u0441\u043e\u043a\u0435\u0442',
                '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

prints(words)
print()
prints(point_u)


