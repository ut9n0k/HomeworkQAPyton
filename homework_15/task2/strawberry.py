from homework_15.task2.product import Product


class Strawberry(Product):
    _product_type = "strawberry"

    def __init__(self):
        self.__color = "Red"
        self.__size = ["Big", "Small"]

    @property
    def get_size(self):
        return self.__size

    def get_product(self, size: str):
        if size == "Big":
            return "You choose big strawberry"
        elif size == "Small":
            return "You choose small strawberry"
