# 3 есть строка переданная в качестве квери параметров
# "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".
# Преобразовать эту строку в словарь где ключем должно быть значение перед =, а значение пары значение после равно
# {name: Amanda......}

query = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
my_dict = {}
seperated = query.split('&')

dict(my_dict.split('=') for my_dict in query.split())

for pare in seperated:

    my_dict.items()
print(my_dict)