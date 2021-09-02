# Создать класс Action. класс должен содержать название действия.
# Создать класс Human где в конструкторе инстанцировать класс действие и присвоить ссылку для поля инстанса Human
# (поле приватное).
# Написать свойство возвращающее действие.
# Перебрать список людей созданных с помощью класса Human и вызвать действие как функцию.
import random

from homework_14.task1.Human import Human

if __name__ == '__main__':

    humans = []
    actions = ["Drinking", "Eating", "Sleeping"]
    name = "Harry", "John", "Marta", "Denny", "Kiki", "Ricky"
    for a in range(3):
        humans.append(Human((random.choice(name)), (random.randint(21, 60)), actions[a]))

    for human in humans:
        print(f"Hello, I'm {human.name}, {human.age} y.o. My hobby is {human.action()}.")
