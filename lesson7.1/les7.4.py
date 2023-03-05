"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
 первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''



    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

    def __add2__(self, other):
        for i in range(len(self.my_list)):
            for i_1 in range(len(other.my_list[i])):
                self.my_list[i][i_1] = self.my_list[i][i_1] + other.my_list[i][i_1]
        return Matrix.__str__(self)
    def __add1__(self, other):
        for i in range(len(self.my_list)):
            for i_1 in range(len(other.my_list[i])):
                self.my_list[i][i_1] = self.my_list[i][i_1] + other.my_list[i][i_1]
        return Matrix.__str__(self)



m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2]])
r = Matrix([[-1, 0, 1, 2], [-1, 0, 1, 3]])
new_r = Matrix([[-2, 0, 2, 1], [-2, 0, 2, 0]])
n = Matrix([[-1, 0], [-1, 0], [0, 1]])
new_n = Matrix([[-2, 0], [-2, 0], [0, 2]])
print(m.__add__(new_m))
print(r.__add2__(new_r))
print(n.__add1__(new_n))