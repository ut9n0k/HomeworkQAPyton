# 3. У вас есть 2 списка имен friends = ["John", "Marta", "James"] и enamies = ["John", "Johnatan", "Artur"].
# Перебрать имена друзей и написать сообщение f"{friend} we are the best friends" если друг не оказался в списке
# имен врагов. И вывести сообщение f"{friend} we are not the friends anymore" если друг оказался в списке врагов.
# Если имя друга James не проверяем его ибо он лучшый друг.

friends = ["John", "Marta", "James"]
enemies = ["John", "Johnathan", "Artur"]

for name in friends:
    if name == 'James':
        print(f"{name} we are the best friends")
    elif name not in enemies:
        print(f"{name} we are the best friends")
    else:
        print(f"{name} we are not the friends anymore")

# Good. But we should not do anything if name if James
