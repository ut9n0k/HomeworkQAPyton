# Задача с пункта 8. Вместо строк в списке друзей должны быть такие же словари как джон и марта.
# Создайте по 2 друга для джона и марты. Выведите в консоль поля Джона и Марты.

john = {
    "full_name": "John John",
    "age": 22,
    "salary": 5000.50,
    "gender": True,
        'friends_john': {
            "friend_1": "Alex",
            "friend_2": "Ivan",
        },
    "coordinates": (50.4851493, 30.4721233)
}
marta = {
    "full_name": "Marta Marta",
    "age": 33,
    "salary": 6000.60,
    "gender": False,
        'friends_marta': {
            "friend_1": "Hanna",
            "friend_2": "Viki"
        },
    "coordinates": (50.4851593, 30.4725233)
}
print(john, marta)
