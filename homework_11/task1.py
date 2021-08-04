# Описать транспортное средство. Можете брать любое на свое усмотрение.
# Хочу видеть наследование (обычное с несколькими уровнями иерархии), абстракцию, сокрытие, инкапсуляцию.

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self):
        self.color = None
        self.wheels = 4
        self.doors = None
        self.engine = True
        self.type_of_engine = None

    @staticmethod
    def moving():
        print("I'm moving!")

    @staticmethod
    def turn_left():
        print("I'm turning left!")

    @staticmethod
    def turn_right():
        print("I'm turning right!")

    @staticmethod
    def stopping():
        print("I'm stopping!")

    @abstractmethod
    def refuel(self):
        """Depends of type of engine"""
        pass


class SerpolletCar(Transport):
    def __init__(self):
        self.doors = 2
        self.color = "Black"
        super().__init__()
        self.type_of_engine = "Steam Engine"

    def refuel(self):
        print("I refuel by steam and magic")


class FormulaOne(SerpolletCar):
    def __init__(self):
        self.color = "Red"
        super().__init__()
        self.type_of_engine = "Internal Combustion Engine"

    def refuel(self):
        print("I refuel by petrol")


if __name__ == "__main__":
    serpollet_car = SerpolletCar()
    formula_one = FormulaOne()

    print(serpollet_car.type_of_engine)
    serpollet_car.refuel()
    print(formula_one.type_of_engine)
    formula_one.refuel()
