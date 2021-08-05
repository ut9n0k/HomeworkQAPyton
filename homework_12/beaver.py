from homework_12.mammal import Mammal


class Beaver(Mammal):
    def __init__(self):
        self.__hobby = "Eating trees"
        self.__childbirth = "Pregnancy"
        self.__lifestyle = True
        super().__init__()

    def make_noise(self):
        return "Uaaa"
