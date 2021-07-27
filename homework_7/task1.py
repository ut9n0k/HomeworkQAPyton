# Написать свою реализацию функции filter.
# Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
# Аннотации дописать самим. Функции должны уметь работать с целыми числами,
# числами с плавающей точкой и строками в качестве элементов последовательностей.
# В качестве последовательностей могут быть переданы списки, кортэжи, словари.
# Буду проверять с помощью майпай аннотации.

from typing import Union

"""
    Function with custom filtering
"""


def filter_for_sequences(callback, sequence: Union[list, tuple, dict]) -> Union[list, tuple, dict, str]:
    result = []
    if type(sequence) == list:
        for item in sequence:
            if callback(item):
                result.append(item)
        return result

    elif type(sequence) == tuple:
        for item in sequence:
            if callback(item):
                result.append(item)
        return tuple(result)

    elif type(sequence) == dict:
        new_dict = {}
        for key, value in sequence.items():
            if callback(value):
                result.append(value)
                new_dict[key] = value
        return new_dict

    else:
        return f"Sorry, your sequence has unsupported type"


if __name__ == "__main__":
    my_list = [10, 200, 3003, 40.44, 500.55]
    my_tuple = ("Bernard", "Brittani", "Bob", "John", "Harold", "Jenny", "Ben")
    my_dict = {
        "Bob": {
            "name": "Bob",
            "lastname": "Bobina",
            "age": 44,
            "salary": 2200.22
        },
        "Ben": {
            "name": "Ben",
            "lastname": "Bebina",
            "age": 22,
            "salary": 400.44
        }
    }
    my_suit = {"Hello", "Bye"}

    # for list
    print(filter_for_sequences(lambda num: num % 2 == 0, my_list))
    # for tuple
    print(filter_for_sequences(lambda word: word.startswith('H'), my_tuple))
    # for dict
    print(filter_for_sequences(lambda item: item["age"] == 44, my_dict))
    print(filter_for_sequences(lambda item: item["name"].endswith('n'), my_dict))
    # for suit
    print(filter_for_sequences(lambda num: num % 2 == 0, my_suit))
