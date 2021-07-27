# Написать свою реализацию функции map
# Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
# Аннотации дописать самим. Функции должны уметь работать с целыми числами,
# числами с плавающей точкой и строками в качестве элементов последовательностей.
# В качестве последовательностей могут быть переданы списки, кортэжи, словари.
# Буду проверять с помощью майпай аннотации.

from typing import Union, Callable, List, Tuple, Dict

"""
    Function for sequences mapping
"""


def map_for_sequences(callback: Callable, sequence: Union[List, Tuple, Dict]):
    result = []
    for items in sequence:
        result.append(callback(items))
    return result


if __name__ == "__main__":
    bob_info = {
            "name": "Bob",
            "lastname": "Bobina",
            "age": 44,
            "salary": 2200.22
        }
    ben_info = {
            "name": "Ben",
            "lastname": "Bebina",
            "age": 22,
            "salary": 400.44
        }

# for list
    print(map_for_sequences(lambda num: num + 100, [10, 200, 3003, 40.44, 500.55]))
# for tuple
    print(map_for_sequences(lambda name: f"Hello, {name}! How are you?", ("Bernard", "Brittani", "Bob", "John")))
# for dict
    print(map_for_sequences(lambda item: (item["name"], item["lastname"]), [ben_info, bob_info]))
