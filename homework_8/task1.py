# 1. Создать декоратор которые принтит в консоль имя функции которая была вызвана. Функция при этом должна работать как
# и задумывалось. К примеру создайте пару функции для арифметических операций суммирования и умножения.
# При вызове этих функций должен возвращаться результат операции и предварительно выводиться в консоль
# имя функции которая была вызвана.

def my_decorator(func):
    def inner(x, y):
        print(f"Function name is: {func.__name__}")
        return func(x, y)

    return inner


@my_decorator
def amount(x, y):
    return x + y


@my_decorator
def multiply(x, y):
    return x * y


print(amount(7, 7))
print(multiply(7, 7))

# Perfect
