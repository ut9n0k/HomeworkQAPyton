# 2 Описать объект Train. Класс должен содержать поля и метод добавления вагонов
# (добавлять нужно именно обьекты экземпляры класса вагон).

# Описать вместе с поездом класс TrainCar (вагон).
# Вагон должен содержать список пассажиров и позволять добавлять пассажиров.
# В вагоне может быть 10 пассажиров к примеру.
# При использовании функции len на вагоне хочу видеть количество пассажиров.
# При использовании len на поезде хочу видеть список вагонов без локомотива.
# У каждого вагона должен быть номер.
# При принте вагона в консоль хочу видеть следующее "[n]" где n номер вагона.

# from homework_13.task2.Train import Train
# from homework_13.task2.TrainCar import TrainCar
from MariaMIshustina.HomeworkQAPyton.homework_13.task2.Train import Train
from MariaMIshustina.HomeworkQAPyton.homework_13.task2.TrainCar import TrainCar

if __name__ == '__main__':
    train = Train(1)
    traincar_1 = TrainCar(1, 10)

    # print(f"Num of the 1st traincar is {traincar_1}")
    # print(train.add_traincar)
    # print(len(traincar_1))
    # print(len(traincar_1))
    # TypeError: 'int' object is not callable
    # well almost works. You should not make magic methods like properties remove decorator -3 points
