class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


class Animal:
    fed = False
    alive = True

    def __init__(self, name):
        self.food = None
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        self.food = food
        if not food.edible:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}.')
        else:
            Animal.fed = True
            print(f'{self.name} съел {food.name}.')


class Predator(Animal):
    def eat(self, food):
        self.food = food
        if not food.edible:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}.')
        else:
            Animal.fed = True
            print(f'{self.name} съел {food.name}.')


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
