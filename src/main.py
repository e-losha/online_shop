class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # умножаем цену на количество и в конце плюсуем их
        total_self = self.price * self.quantity
        total_other = other.price * other.quantity

        return total_self + total_other

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        # защита от нуля и минуса
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # если ставим цену дешевле спрашиваем подтверждение
        if new_price < self.__price:
            user_answer = (
                input("Указанная цена ниже текущей. Продолжить? (y/n): ")
                .strip()
                .lower()
            )
            if user_answer != "y":
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_dict):
        # создаем объект Product из словаря через распаковку
        return cls(**product_dict)


class Category:
    category_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self._products = list(products)

        # увеличиваем чисто категорий при инициализации
        Category.category_count += 1
        # считаем количество продуктов внутри категории
        Category.products_count += len(products)

    def __str__(self):
        # берем именно количество в каждом продукте отдельно и суммируем их
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        # сделал свой итератор для --- for product in category: ---
        return CategoryIterator(self._products)

    def add_product(self, new_product):
        # проверяем есть ли у нас уже такой продукт
        for product in self._products:
            # если нашли совпадение - количество плюсуем, цену берем максимальную из двух
            if product.name == new_product.name:
                product.quantity += new_product.quantity
                product.price = max(product.price, new_product.price)
                break
        # если не нашли - добавляет продукт
        else:
            self._products.append(new_product)

            Category.products_count += 1

    @property
    def products(self):
        # возвращает строковое представление всех товаров в категории
        # каждый объект Product преобразуется в строку через его __str__
        return "\n".join(str(product) for product in self._products)


class CategoryIterator:

    def __init__(self, products: list[Product]):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
