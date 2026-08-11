import pytest

from src.main import (
    BaseEntity,
    BaseProduct,
    Category,
    LawnGrass,
    MixinLog,
    Order,
    Product,
    Smartphone,
)


def test_product_init(my_product):
    assert my_product[0].name == "Арбуз"
    assert my_product[1].description == "оранжевый"
    assert my_product[2].price == 55
    assert my_product[3].quantity == 5


def test_category_init(my_category):
    assert my_category.name == "Фрукты"
    assert len(my_category._products) == 4
    assert my_category._products[0].name == "Арбуз"


def test_counter_one(my_category):
    assert Category.category_count == 1
    assert Category.products_count == 4


def test_counter_multiple():
    product_apple = Product("Яблоко", "красное", 45, 5)
    category_fruits = Category("Фрукты", "обычные", [product_apple])

    assert Category.category_count == 1
    assert Category.products_count == 1

    product_tomato = Product("Помидор", "красный", 35, 8)
    category_fruits = Category("Овощи", "стандартные", [product_tomato])

    assert Category.category_count == 2
    assert Category.products_count == 2


def test_counter_with_multiple_products():
    product_apple = Product("Яблоко", "красное", 45, 5)
    product_banana = Product("Банан", "желтый", 65, 2)
    product_orange = Product("Апельсин", "оранжевый", 55, 6)

    category = Category(
        "Фрукты", "спелые", [product_apple, product_banana, product_orange]
    )

    assert Category.category_count == 1
    assert Category.products_count == 3


def test_price_setter():
    my_product = Product("Яблоко", "красное", 45, 5)

    my_product.price = -1
    assert my_product.price == 45

    my_product.price = 0
    assert my_product.price == 45

    my_product.price = 50
    assert my_product.price == 50


def test_new_product():
    product_dict = {
        "name": "55 QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7,
    }

    my_new_product = Product.new_product(product_dict)
    assert my_new_product.name == "55 QLED 4K"
    assert my_new_product.description == "Фоновая подсветка"
    assert my_new_product.price == 123000.0
    assert my_new_product.quantity == 7


def test_products_getter(my_category):
    result = my_category.products

    assert result == (
        "Арбуз, 300 руб. Остаток: 10 шт.\n"
        "Мандарин, 25 руб. Остаток: 25 шт.\n"
        "Яблоко, 55 руб. Остаток: 15 шт.\n"
        "Банан, 45 руб. Остаток: 5 шт."
    )


def test_add_product(my_category):
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)
    my_category.add_product(new_product1)

    assert my_category._products[0].price == 500
    assert my_category._products[0].quantity == 13
    assert len(my_category._products) == 4

    new_product2 = Product("Киви", "зеленый", 400, 10)
    my_category.add_product(new_product2)

    assert my_category._products[4].name == "Киви"
    assert my_category._products[4].description == "зеленый"
    assert my_category._products[4].price == 400
    assert my_category._products[4].quantity == 10
    assert len(my_category._products) == 5


def test_product_str():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)

    assert str(new_product1) == "Арбуз, 500 руб. Остаток: 3 шт."


def test_product_add_basic():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)
    new_product2 = Product("Арбуз", "зелено-красный", 400, 10)

    assert new_product1 + new_product2 == 5500


def test_product_add_zero():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 0)
    new_product2 = Product("Киви", "зеленый", 400, 10)

    assert new_product1 + new_product2 == 4000


def test_product_add_commutative():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 2)
    new_product2 = Product("Киви", "зеленый", 400, 10)

    assert new_product1 + new_product2 == new_product2 + new_product1


def test_product_add_same_product():
    new_product1 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        "efficient",
        "15",
        "512GB",
        "Gray",
    )
    new_product2 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        "efficient",
        "Note 11",
        "1024GB",
        "Синий",
    )

    assert new_product1 + new_product2 == 2114000


def test_product_add_diff_products():
    new_product1 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        "efficient",
        "15",
        "512GB",
        "Gray",
    )
    new_product2 = LawnGrass("Трава", "газонная", 500, 20, "Poland", "3 weeks", "Green")

    assert TypeError("Нельзя складывать разные товары")


def test_product_smartphone_init(my_product_smartphone):
    assert my_product_smartphone.name == "Iphone 15"
    assert my_product_smartphone.description == "512GB, Gray space"
    assert my_product_smartphone.price == 210000.0
    assert my_product_smartphone.quantity == 8
    assert my_product_smartphone.efficiency == "efficient"
    assert my_product_smartphone.model == "15"
    assert my_product_smartphone.memory == "512GB"
    assert my_product_smartphone.color == "Gray"


def test_product_lawngrass_init(my_product_lawngrass):
    assert my_product_lawngrass.name == "Трава"
    assert my_product_lawngrass.description == "газонная"
    assert my_product_lawngrass.price == 500
    assert my_product_lawngrass.quantity == 20
    assert my_product_lawngrass.country == "Poland"
    assert my_product_lawngrass.germination_period == "3 weeks"
    assert my_product_lawngrass.color == "Green"


def test_base_product():
    with pytest.raises(TypeError):
        BaseProduct("Арбуз", "зелено-красный", 500, 3)


def test_product_logging(capsys):
    product = Product("Арбуз", "зелено-красный", 500, 3)
    captured = capsys.readouterr()
    assert "Product('Арбуз', 'зелено-красный', 500, 3)" in captured.out


def test_product_repr():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)
    assert repr(new_product1) == "Product('Арбуз', 'зелено-красный', 500, 3)"


def test_smartphone_logging(capsys):
    smartphone = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        "efficient",
        "15",
        "512GB",
        "Gray",
    )
    captured = capsys.readouterr()
    assert "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)" in captured.out


def test_base_entity():
    with pytest.raises(TypeError):
        BaseEntity()


def test_order_init():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)
    new_order1 = Order(new_product1, 3)

    assert new_order1.product == new_product1
    assert new_order1.quantity == 3


def test_order_str():
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)
    new_order1 = Order(new_product1, 5)

    assert (
        str(new_order1)
        == "Заказ: Арбуз, 500 руб. Остаток: 3 шт., количество: 5, итоговая стоимость: 2500"
    )
