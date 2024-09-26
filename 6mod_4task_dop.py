# Дополнительное практическое задание по модулю
import math

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *args_sides):
        self.__sides = args_sides               # (список сторон (целые числа))
        if self.__is_valid_color(color) == color:
            self.__color = color                # список цветов в формате RGB
        self.__is_valid_sides(*args_sides)

    def get_color(self):
        return list[self.__color]

    def __is_valid_color(self, new_color): # проверяет корректность переданных значений перед установкой нового цвета
        flag = 0
        for i in new_color:
            if 255 >= i >= 0 == i % 1:
                flag += 1
        if flag == 3:
            self.__color = new_color
            return self.__color
        else:
            print('Не корректные параметры цвета: r, g и b - целые числа в диапазоне от 0 до 255 (включительно)')

    def set_color(self, *args_new_color):
        self.__is_valid_color(args_new_color)

    def __is_valid_sides(self, *args_sides):
        flag = 0
        for i in args_sides:
            if i > 0 and i % 1 == 0:
                flag += 1
        if flag == len(args_sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return float(sum(self.get_sides()))

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            print('Введено не корректное значение, изменение не произойдет')


class Circle(Figure):
    sides_count = 1
    __radius = Figure.__len__() / (2 * math.pi) #  ???

    # def __init__(self, color, *args_sides):
    #     super().__init__(color, *args_sides)
    #     self.__radius = Figure.__len__() / (2 * math.pi)





F = Figure((0, 150, 255), 15, 2)
# F.set_color(0, 1, 250)
# print(F._Figure__is_valid_sides(1))
# print(F.get_sides())
# print(F.__len__())
# F.set_sides(9)

C = Circle((1, 2, 3), 6, 5)
print()
print(C.__len__())





