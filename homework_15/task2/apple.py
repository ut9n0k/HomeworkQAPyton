from homework_15.task2.product import Product


class Apple(Product):
    _product_type = "apple"

    def __init__(self):
        self.__color = "White"
        self.__size = ["Big", "Small"]

    @property
    def get_size(self):
        return self.__size

    def get_product(self, size: str):
        if size == "Big":
            return "You choose big apple"
        elif size == "Small":
            return "You choose small apple"
