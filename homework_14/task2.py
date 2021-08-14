# Создайте итератор принимающий последовательность и умеющий перебирать значения по заданному диапазону.
# CustomIterator(sequence, start_index, end_index)

class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index - 1
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__sequence) > self.__start_index <= self.__end_index:
            element = self.__sequence[self.__start_index]
            self.__start_index += 1
            return element
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 9)
    iterator = iter(custom_iterator)
    for item in iterator:
        print(item)
