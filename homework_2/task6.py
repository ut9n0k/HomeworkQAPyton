# У вас есть группа людей с неуникальными именами.
# Сформируйте список не повторяющихся имен (для этой задачи нельзя использовать set.
# Если в списке есть 2 джона нужно взять лишь одного из них.
# "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow")

list = ['John', 'Ivan', 'Marta', 'Marishka', 'Hou', 'John']

list_new = []
for item in list:
    if item not in list_new:
        list_new.append(item)

for item in list_new:
    print(item)

# Good. I think this solution is little bit over engineered.
# So take a look how it could be one with dicts

# print(list({}.fromkeys(list_of_guests).keys()))
