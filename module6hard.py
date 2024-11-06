from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=True):
        self.__color = __color
        self.__sides = __sides
        self.filled = filled
        super().__init__()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        list = [r, g, b]
        if 0 <= list[0] <= 255 and 0 <= list[1] <= 255 and 0 <= list[2] <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        for i in sides:
            if i > 0 and len(sides) == len(self.__sides):
                return True
            else:
                return False

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):  # периметр
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(self.__sides) != self.sides_count:
            self.__sides = self.__sides
        else:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__() / (2 * pi)

    def get_square(self):
        return pi * ((self.__len__() / 2) ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a = self.__sides[0]  # сторона треуг-ка 1
        b = self.__sides[1]  # сторона треуг-ка 2
        c = self.__sides[2]  # сторона треуг-ка 3
        p = (a + b + c) / 2  # полупериметр треуг-ка
        S = sqrt(p(p - a)(p - b)(p - c))  # площадь треуг-ка
        return S


class Cube(Figure):
    sides_count = 12 #кол-во рёбер куба

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides, filled=True)
        self.__sides = self.sides_count * __sides

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
