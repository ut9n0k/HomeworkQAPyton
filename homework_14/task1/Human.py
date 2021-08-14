from homework_14.task1.Action import Action


class Human:
    def __init__(self, name: str, age: int, action: str):
        self.__name = name
        self.__age = age
        self.__action = Action(action)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def action(self) -> Action:
        return self.__action
