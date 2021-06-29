# 8. Создайте 2 переменные john, marta. Переменные должны быть словарями с ключами:
# full_name, age, salary, gender, friends, coordinates.
# Требования к структуре:
# Full_name - полное имя
# Age - возраст
# Salary - зароботная плата
# Gender - пол человека (используйте булев тип)
# Friends - список друзей из задачи 6
# Coordinates - долгота и широта из задачи 7
# Вывести в консоль джона и марту ключ и значение: “key => value” где key это ключ пары из словаря
# а value это значение пары из словаря.

john = {
    "full_name": "John John",
    "age": 22,
    "salary": 5000.50,
    "gender": True,
    "friends": ["Alex", "Harry", "Ivan"],
    "coordinates": (50.4851493, 30.4721233)
}
marta = {
    "full_name": "Marta Marta",
    "age": 33,
    "salary": 6000.60,
    "gender": False,
    "friends": ["Hanna", "Rio", "Viki"],
    "coordinates": (50.4851593, 30.4725233)
}
for a, b in john.items():
    print(a, b)

for c, d in marta.items():
    print(c, d)

# you can print dicts in next way^
# for key, value in marta.items():
#     print(f"{key} => {value}")
