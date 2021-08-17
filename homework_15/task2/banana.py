from homework_15.task2.product import Product


class Banana(Product):
    _product_type = "banana"

    def __init__(self):
        self.__color = "Yellow"
        self.__size = ["Big", "Small"]

    @property
    def get_size(self):
        return self.__size

    def get_product(self, size: str):
        if size == "Big":
            return "You choose big banana"
        elif size == "Small":
            return "You choose small banana"
