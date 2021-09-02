from homework_15.task2.product import Product


class Celery(Product):
    _product_type = "cellery"

    def __init__(self):
        self.__color = "Green"
        self.__size = ["Big", "Small"]

    @property
    def get_size(self):
        return self.__size

    def get_product(self, size: str):
        if size == "Big":
            return "You choose big cellery"
        elif size == "Small":
            return "You choose small cellery"
