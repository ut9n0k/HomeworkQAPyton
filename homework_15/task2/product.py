# У вас есть магазин. Хочу что бы ваш магазин давал мне необходимый товар по приметам.
# Market класс должен содержать метод возвращающий товар. Соответственно могут быть следующие товары:
# Apple, Banana, Cellery, Strawbarry.
# Каждый из этих продуктов имеет общего родителя Product который абстрактный класс. (фабричный метод)

from abc import ABC, abstractmethod


class Product(ABC):
    _product_type: str = ""

    @abstractmethod
    def get_product(self, size: str):
        pass
