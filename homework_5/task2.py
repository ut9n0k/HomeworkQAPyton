# Используя созданный файл в задаче 1 прочитать файл и произвести математические операции над каждым элементом.
# Результат операции вывести в консоль. Использовать импорты для импортирования из модуля первой задачи нельзя.

import os
os.chdir("./test/data")

import pickle

with open("text.txt", "rb") as file:
    byte_text = file.read()
    q = pickle.loads(byte_text)

for a in q:
    if a[2] == 1:
        print(a[0] + a[1])
    elif a[2] == 2:
        print(a[0] - a[1])
    elif a[2] == 3:
        print(a[0] * a[1])
