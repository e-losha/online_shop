import json
import os
from pathlib import Path

from src.main import Category, Product


def read_json(path: str | Path) -> list[dict]:
    # превращаем относительный путь в полный абсолютный путь,
    # чтобы Python точно понимал, где лежит файл
    full_path = os.path.abspath(path)

    # открываем json-файл в режиме чтения
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def create_objects_from_json(data: list[dict]) -> list[Category]:
    # создаем пустой список куда будет складывать объекты Category
    categories = []

    # перебираем каждую категорию по json
    for category in data:
        # для каждой категории создаем отдельный список продуктов
        products = []

        for product in category["products"]:
            # создаем объект Product из словаря
            # **product = распаковка словаря:
            # {"name": "...", "price": ...}
            # превращается в:
            # Product(name="...", price=...)
            product_obj = Product(**product)

            # добавляем созданный объект Product в список products
            products.append(product_obj)

        # создаем объект Category,
        # передаем:
        # - имя категории
        # - описание категории
        # - список уже созданных объектов Product
        category_obj = Category(
            name=category["name"],
            description=category["description"],
            products=products,
        )

        # добавляем готовую категорию в общий список categories
        categories.append(category_obj)

    return categories
