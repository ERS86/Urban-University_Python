class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, __model, __engine_power, __color, __owner):
        self.__owner = str(__owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f'"Модель: {self.__model}"'

    def get_horsepower(self):
        return f'"Мощность двигателя: {self.__engine_power}"'

    def get_color(self):
        return f'"Цвет: {self.__color}"'

    def print_info(self):
        print   (f'"Модель: {self.__model}"\n'
                f'"Мощность двигателя: {self.__engine_power}"\n'
                f'"Цвет: {self.__color}"\n'
                f'"Владелец: {self.__owner}"\n')

    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'"Нельзя сменить цвет на {new_color}"')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Toyota Mark II', 500, 'blue', 'Fedos')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
