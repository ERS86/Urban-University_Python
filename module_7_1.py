class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def add(self, *products):
        for i in products:
            i = str(i)
            if i not in self.get_products():
                products_txt = open(self.__file_name, 'a')
                products_txt.write(f'{i} \n')
                products_txt.close()
            else:
                print(f'Продукт {i} уже есть в магазине.')

    def get_products(self):
        products_txt = open(self.__file_name, 'r')
        return products_txt.read()


s1 = Shop('', '', '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
