# Используя созданный файл в задаче 1 прочитать файл и произвести математические операции над каждым элементом.
# Результат операции вывести в консоль. Использовать импорты для импортирования из модуля первой задачи нельзя.

import os
import pickle

os.chdir("./test/data")

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

# well good but not clear what is a and q. So take a look how it could
# be solved cleaner.
with open("text.txt", "rb") as file:
    byte_text = file.read()
    operations = pickle.loads(byte_text)

for operation in operations:
    left, right, operator = operation
    if operator == 1:
        print(f"{left} + {right} = {left + right}")
    elif operator == 2:
        print(f"{left} - {right} = {left - right}")
    elif operator == 3:
        print(f"{left} * {right} = {left * right}")

# spend more time for naming variables and take a look how it could
# be unpacked like I made
