# #     Опишите любой объект на ваш выбор в классе. Основные требования к объекту:
# #     объект должен содержать некое поведение которое меняет его состояние
# #     объект должен быть простым то бишь только по средством своего поведения менять свое состояние.
# #     должны присутствовать следующие постулаты: абстракция, наследование, инкапсуляция, сокрытие
# # Проявите свою фантазию. Балы сильно снимать не буду.

from abc import ABC, abstractmethod


class Mammal(ABC):
    def __init__(self):
        self.noise = None
        self.tail = True
        self.hobby = None
        self.childbirth = None
        self.feeding = "With milk"
        self.lifestyle = None

    @abstractmethod
    def make_noise(self):
        """
            reproduce some noise
        """
        pass

# Good. If you want to share this fields for child classes you can make
# them protected
