# Написать свою реализацию функции filter.
# Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
# Аннотации дописать самим. Функции должны уметь работать с целыми числами,
# числами с плавающей точкой и строками в качестве элементов последовательностей.
# В качестве последовательностей могут быть переданы списки, кортэжи, словари.
# Буду проверять с помощью майпай аннотации.

from typing import Union, Callable, List, Tuple, Dict

"""
    Function for sequences filtering
"""


def filter_for_sequences(callback: Callable, sequence: Union[List, Tuple, Dict]):
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
    print(filter_for_sequences(lambda num: num % 2 == 0, [10, 200, 3003, 40.44, 500.55]))
    # for tuple
    print(filter_for_sequences(lambda word: word.startswith('B'), ("Bernard", "Brittani", "Bob", "John")))
    # for dict
    print(filter_for_sequences(lambda item: item["name"].endswith('n'), [bob_info, ben_info]))
