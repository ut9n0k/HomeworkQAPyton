# 2. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square(a):
    p = a * 4
    s = a * a
    d = (2 ** 0.5) * a

    answers = f"Периметр квадрата: {p}, Площадь квадрата: {s}, Диагональ квадрата: {d}"
    return answers


print(square(5))

# Not bad but tuple with 3 numbers should be in the return value instead of string)
# also hard to understand what is a, s, d.
