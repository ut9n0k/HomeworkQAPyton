# Задача с пункта 8. Вместо строк в списке друзей должны быть такие же словари как джон и марта.
# Создайте по 2 друга для джона и марты. Выведите в консоль поля Джона и Марты.
alex = {
    "full_name": "Alex Alex",
    "age": 44,
    "salary": 5040.40,
    "gender": True,
    "friends": ["Ivan", "John"],
    "coordinates": (50.4851499, 30.4721239)
}
ivan = {
    "full_name": "Ivan Ivan",
    "age": 10,
    "salary": 10000.40,
    "gender": True,
    "friends": ["Alex", "John"],
    "coordinates": (50.4851498, 30.4791239)
}
john = {
    "full_name": "John John",
    "age": 22,
    "salary": 5000.50,
    "gender": True,
    "friends": [alex, ivan],
    "coordinates": (50.4851493, 30.4721233)
}

hanna = {
    "full_name": "Hanna Hanna",
    "age": 39,
    "salary": 699.99,
    "gender": False,
    "friends": ["Marta", "Viki"],
    "coordinates": (60.4851593, 60.4725233)
}
viki = {
    "full_name": "Viki Viki",
    "age": 66,
    "salary": 66.66,
    "gender": False,
    "friends": ["Hanna", "Marta"],
    "coordinates": (50.4851566, 30.4725266)
}
marta = {
    "full_name": "Marta Marta",
    "age": 33,
    "salary": 6000.60,
    "gender": False,
    "friends": [hanna, viki],
    "coordinates": (50.4851593, 30.4725233)
}

print(john.items())
print(marta.items())
