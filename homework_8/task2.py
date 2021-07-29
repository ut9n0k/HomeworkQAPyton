# Создайте функцию которая способна вернуть квадраты четных элементов для диапазона  от 0 до 1000000000 включительно.
# Решение должно отрабатывать и не фризить ваш комп.

def my_gen():
    num = 0
    while num <= 1000000000:
        yield num ** 2
        num += 2


range_square = my_gen()

print(next(range_square))
print(next(range_square))
print(next(range_square))
print(next(range_square))
# perfect