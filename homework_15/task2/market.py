from homework_15.task2.product import Product
from homework_15.task2.apple import Apple
from homework_15.task2.banana import Banana
from homework_15.task2.cellery import Celery
from homework_15.task2.strawberry import Strawberry


class Market:
    @staticmethod
    def get_product(product_type: str) -> Product:
        if product_type == "apple":
            return Apple()
        elif product_type == "banana":
            return Banana()
        elif product_type == "cellery":
            return Celery()
        elif product_type == "strawberry":
            return Strawberry()
        else:
            raise Exception("We don't sell this product")


if __name__ == '__main__':
    cellery = Market.get_product("cellery")
    print(cellery.get_product("Big"))
