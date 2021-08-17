# Описать объект на ваше усмотрение. Экземпляр объекта может быть лишь один в системе.
# Хочу увидеть паттерн синглтон но статическое поле инстанс хочу видеть приватным.

from homework_15.task1.singleton import singleton


@singleton
class Human:
    def __init__(self, name: str, last_name: str, age: int, alive: bool):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__alive = alive


if __name__ == '__main__':
    harry = Human("Harry", "Dubuoi", 42, True)
    ping = Human("Ping", "Pong", 33, False)
    print(harry)
    print(ping)
