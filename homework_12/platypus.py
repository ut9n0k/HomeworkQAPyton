from homework_12.beaver import Beaver


class Platypus(Beaver):
    def __init__(self):
        self.__hobby = "Swimming"
        self.__childbirth = "Lay eggs after 2 weeks"
        self.__lifestyle = False
        self.__x = 0
        self.__y = 0
        self.__z = 0
        super().__init__()

    def make_noise(self):
        return "Urrr"

    def move(self, direction: str, distance: int):
        if direction == "dive":
            if self.__z > 0:
                self.__z -= distance
        elif direction == "forward":
            self.__y += distance
        elif direction == "left":
            self.__x -= distance
        elif direction == "right":
            self.__x += distance
        elif direction == "back":
            self.__y -= distance
        elif direction == "get out":
            if self.__z < 0:
                self.__z += distance
