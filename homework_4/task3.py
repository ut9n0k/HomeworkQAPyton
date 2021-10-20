# 3 есть строка переданная в качестве квери параметров
# "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".
# Преобразовать эту строку в словарь где ключем должно быть значение перед =
# а значение пары значение после равно {name: Amanda......}

query = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".strip()
my_dict = {}
pairs = (query.split('&'))
print(pairs)

for pair in pairs:
    if pair != '':
        a, b = pair.split('=', maxsplit=1)
        my_dict[a] = b

print(my_dict)

# Excellent
