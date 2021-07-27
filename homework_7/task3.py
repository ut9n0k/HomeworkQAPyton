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
    # Well good but main purpose of reduce in other things. Take a look how is look like reduce
    # def custom_reduce(callback: Callable, sequence):
    #     element = sequence[0]
    #     counter = 0
    #     for _ in sequence:
    #         if len(sequence) - 1 == counter:
    #             break
    #         counter += 1
    #         element = callback(element, sequence[counter])
    #     return element

    # custom_reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
    pass