# У вас есть две группы людей. В одной группе состоят всеядные люди в другой лишь вегетарианцы.
# Всеядный является вегетарианцем но вегетарианец не является всеядным.
# Вывести список гостей которые могут есть овощи и зелень.

love_all_meals = ['Jerry', 'Mark', 'Ivan', 'Hulio']
love_only_veggies = ['Agatha', 'Dora', 'Hrisha']
can_eat_veggies = []

can_eat_veggies.extend(love_only_veggies)
can_eat_veggies.extend(love_all_meals)

print(can_eat_veggies)

# Good
