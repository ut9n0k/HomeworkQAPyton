# 1.у вас есть список элементов [1, 2, 3, 4, 5, 6, 7, 8]. Перебрать список используя foreach цыкл .
# Элемент с нечетным индексом поместить в новый список кортежей где первый элемент это индекс а второй это значение.
# [(index, value)]. соответственно элементы с четным индексом поместить в другой список кортежей с тем же
# форматом что и в случае с нечетными индексами.

my_list = [1, 2, 3, 1, 4, 5, 2, 6, 7, 8]
a = []
b = []

for number in my_list:
    if my_list.index(number) % 2 == 0:
        a.append((my_list.index(number), number))
    else:
        b.append((my_list.index(number), number))

print(a, b, sep='\n')

# Good. But what will be if I will add some more elements which will duplicate
# some of existing?
