class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """
        Считывает все продукты из файла и возвращает их как единую строку.
        """
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        """
        Добавляет новые продукты в магазин, если их ещё нет.
        """
        current_products = self.get_products().split('\n')
        current_names = set()
        for line in current_products:
            if line.strip():
                parts = line.split(', ')
                if len(parts) >= 1:
                    current_names.add(parts[0])

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name not in current_names:
                    file.write(f'{product}\n')
                    current_names.add(product.name)
                else:
                    print(f'Продукт {product} уже есть в магазине')


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())