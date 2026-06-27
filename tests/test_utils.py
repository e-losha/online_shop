import json

from src.main import Category, Product
from src.utils import create_objects_from_json, read_json


def test_read_json(tmp_path):
    json_file = tmp_path / "test.json"

    my_data = [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации, "
                "но и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(my_data, file)

    result = read_json(json_file)

    assert result == my_data


def test_create_objects_from_json():
    my_data = [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации, "
                "но и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    result = create_objects_from_json(my_data)

    result = create_objects_from_json(my_data)

    assert len(result) == 1

    category = result[0]

    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни"
    )

    assert len(category._products) == 1

    product = category._products[0]

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
