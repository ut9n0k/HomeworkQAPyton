from typing import List

from TrainCar import TrainCar


class Train:
    def __init__(self, locomotive_num: int):
        self.__locomotive_num = locomotive_num
        self.__traincars: List[TrainCar] = list()

    def add_traincar(self, traincar: TrainCar):
        return self.__traincars.append(traincar)

    @property
    def __len__(self):
        return len(self.__traincars)

    @property
    def traincars(self):
        return self.__traincars

    @property
    def locomotive_num(self):
        return len(self.__traincars) - 1
