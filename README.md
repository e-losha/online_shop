# Учебный проект по Python "online_shop".

## Описание:

в разработке

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/eloosha/online_shop.git
```

2. Установите зависимости:

```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:

```
python manage.py migrate
```

4. Запустите локальный сервер:

```
python manage.py runserver
```

## Использование:

1. В main.py находятся классы: Product, Category, а так же классы наследники от Product: Smartphone(Product) и LawnGrass(Product).
2. В utils.py находятся функции чтения файлов JSON
3. В test_main.py, conftest.py находятся тесты и фикстуры.

## Тестирование

Для запуска тестов используется 'pytest'.

## Запуск тестов

```bash
pytest
```