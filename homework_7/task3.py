# Написать свою реализацию функции reduce
# Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
# Аннотации дописать самим. Функции должны уметь работать с целыми числами,
# числами с плавающей точкой и строками в качестве элементов последовательностей.
# В качестве последовательностей могут быть переданы списки, кортэжи, словари.
# Буду проверять с помощью майпай аннотации.

from typing import Union

"""
    Function for sequences reducing
"""


def reduce_for_sequences(callback, sequence: Union[list, tuple, dict]) -> Union[list, tuple, dict]:
    result = []
    for items in sequence:
        result.append(items) if callback(items) else None
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
        "lastname": "Benini",
        "age": 22,
        "salary": 400.44
    }
# for list
print(reduce_for_sequences(lambda num: num ** 2, [10, 200, 3003, 40.44, 500.55]))
# for tuple
print(reduce_for_sequences(lambda name: f"Hello, {name}! How are you?", ("Bernard", "Brittani", "Bob", "John")))
# for dict
print("Sorry, but I don't know how this method works with dicts, so I passed it. Don't be angry, please T-T")
