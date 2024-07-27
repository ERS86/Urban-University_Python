'''
КАК!!!!!! РЕШИТЬ НЕСООТВЕТСТВИЕ В ПОСЛЕДОВАТЕЛЬНОСТИ МЕТОДОВ(модель,мощность,цвет)
И ПОСЛЕДОВАТЕЛЬНОСТИ ПРИНИМАЕМЫХ ДАННЫХ (имя, модель, цвет, мощность)
И ПОСЛЕДОВАТЕЛЬНОСТИ ВЫВОДА модель,мощность,цвет,имя!!!!!!!!

заявленных в условии и примере
????????????????????????????????????????????????????????????????????????????????????
'''

class Vehicle:

    def __init__(self, __model, __engine_power, __color, owner,):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    __COLOR_VARIANTS = ('red', 'orange', 'yellow', 'green', 'blue', 'darkblue', 'violet', 'black')

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print ( f'Модель: {self.__model},\n'
                f'Мощность двигателя: {self.__engine_power},\n'
                f'Цвет: {self.__color},\n'
                f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Toyota Mark II',   500,'blue','Fedos')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()