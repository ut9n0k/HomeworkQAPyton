# 1 Описать любой объект на ваш выбор в классе. Хочу что бы объект распечатывался в консоль в следующем формате:
# class_name: {
# key: value
# }
# Где class_name - имя вашего класса, key - имя поля, value - значение поля.

class Animal:
    def __init__(self, science_class: str, order: str, food: str, existence: str):
        self.Science_Class = science_class
        self.Order = order
        self.Food = food
        self.Existence = existence

    def __str__(self):
        out_str = f"{self.__class__.__name__}: {{"
        for key, value in self.__dict__.items():
            out_str += f"\n\t{key}: {value}"
        out_str += f"\n}}\n\n"
        return out_str


if __name__ == '__main__':
    human = Animal(
        "Mammals",
        "Primates",
        "Everything",
        "On the land"
    )
    frog = Animal(
        "Amphibians",
        "Anura",
        "Bugs",
        "In the water"
    )

    print(human, frog)
